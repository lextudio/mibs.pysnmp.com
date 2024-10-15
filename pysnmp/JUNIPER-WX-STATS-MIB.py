# SNMP MIB module (JUNIPER-WX-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-WX-GLOBAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:29 2024
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

(jnxWxGrpStats,) = mibBuilder.importSymbols(
    "JUNIPER-WX-GLOBAL-MIB",
    "jnxWxGrpStats")

(jnxWxGrpStatusAppId,
 jnxWxGrpStatusRemoteWxId) = mibBuilder.importSymbols(
    "JUNIPER-WX-STATUS-MIB",
    "jnxWxGrpStatusAppId",
    "jnxWxGrpStatusRemoteWxId")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxWxGrpStatsSys_ObjectIdentity = ObjectIdentity
jnxWxGrpStatsSys = _JnxWxGrpStatsSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxWxGrpStatsSys.setStatus("current")
_JnxWxGrpStatsSysPt_ObjectIdentity = ObjectIdentity
jnxWxGrpStatsSysPt = _JnxWxGrpStatsSysPt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysPt.setStatus("current")
_JnxWxGrpStatsSysPtAppDefMatchBytes_Type = Counter64
_JnxWxGrpStatsSysPtAppDefMatchBytes_Object = MibScalar
jnxWxGrpStatsSysPtAppDefMatchBytes = _JnxWxGrpStatsSysPtAppDefMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 1),
    _JnxWxGrpStatsSysPtAppDefMatchBytes_Type()
)
jnxWxGrpStatsSysPtAppDefMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysPtAppDefMatchBytes.setStatus("current")
_JnxWxGrpStatsSysPtAppDefMatchPkts_Type = Counter64
_JnxWxGrpStatsSysPtAppDefMatchPkts_Object = MibScalar
jnxWxGrpStatsSysPtAppDefMatchPkts = _JnxWxGrpStatsSysPtAppDefMatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 2),
    _JnxWxGrpStatsSysPtAppDefMatchPkts_Type()
)
jnxWxGrpStatsSysPtAppDefMatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysPtAppDefMatchPkts.setStatus("current")
_JnxWxGrpStatsSysPtNoRemoteWxBytes_Type = Counter64
_JnxWxGrpStatsSysPtNoRemoteWxBytes_Object = MibScalar
jnxWxGrpStatsSysPtNoRemoteWxBytes = _JnxWxGrpStatsSysPtNoRemoteWxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 3),
    _JnxWxGrpStatsSysPtNoRemoteWxBytes_Type()
)
jnxWxGrpStatsSysPtNoRemoteWxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysPtNoRemoteWxBytes.setStatus("current")
_JnxWxGrpStatsSysPtNoRemoteWxPkts_Type = Counter64
_JnxWxGrpStatsSysPtNoRemoteWxPkts_Object = MibScalar
jnxWxGrpStatsSysPtNoRemoteWxPkts = _JnxWxGrpStatsSysPtNoRemoteWxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 4),
    _JnxWxGrpStatsSysPtNoRemoteWxPkts_Type()
)
jnxWxGrpStatsSysPtNoRemoteWxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysPtNoRemoteWxPkts.setStatus("current")
_JnxWxGrpStatsSysPtNonTcpProtoBytes_Type = Counter64
_JnxWxGrpStatsSysPtNonTcpProtoBytes_Object = MibScalar
jnxWxGrpStatsSysPtNonTcpProtoBytes = _JnxWxGrpStatsSysPtNonTcpProtoBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 5),
    _JnxWxGrpStatsSysPtNonTcpProtoBytes_Type()
)
jnxWxGrpStatsSysPtNonTcpProtoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysPtNonTcpProtoBytes.setStatus("current")
_JnxWxGrpStatsSysPtNonTcpProtoPkts_Type = Counter64
_JnxWxGrpStatsSysPtNonTcpProtoPkts_Object = MibScalar
jnxWxGrpStatsSysPtNonTcpProtoPkts = _JnxWxGrpStatsSysPtNonTcpProtoPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 6),
    _JnxWxGrpStatsSysPtNonTcpProtoPkts_Type()
)
jnxWxGrpStatsSysPtNonTcpProtoPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysPtNonTcpProtoPkts.setStatus("current")
_JnxWxGrpStatsSysPtNonIpBytes_Type = Counter64
_JnxWxGrpStatsSysPtNonIpBytes_Object = MibScalar
jnxWxGrpStatsSysPtNonIpBytes = _JnxWxGrpStatsSysPtNonIpBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 7),
    _JnxWxGrpStatsSysPtNonIpBytes_Type()
)
jnxWxGrpStatsSysPtNonIpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysPtNonIpBytes.setStatus("current")
_JnxWxGrpStatsSysPtNonIpPkts_Type = Counter64
_JnxWxGrpStatsSysPtNonIpPkts_Object = MibScalar
jnxWxGrpStatsSysPtNonIpPkts = _JnxWxGrpStatsSysPtNonIpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 8),
    _JnxWxGrpStatsSysPtNonIpPkts_Type()
)
jnxWxGrpStatsSysPtNonIpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysPtNonIpPkts.setStatus("current")
_JnxWxGrpStatsSysPtFragIpBytes_Type = Counter64
_JnxWxGrpStatsSysPtFragIpBytes_Object = MibScalar
jnxWxGrpStatsSysPtFragIpBytes = _JnxWxGrpStatsSysPtFragIpBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 9),
    _JnxWxGrpStatsSysPtFragIpBytes_Type()
)
jnxWxGrpStatsSysPtFragIpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysPtFragIpBytes.setStatus("current")
_JnxWxGrpStatsSysPtFragIpPkts_Type = Counter64
_JnxWxGrpStatsSysPtFragIpPkts_Object = MibScalar
jnxWxGrpStatsSysPtFragIpPkts = _JnxWxGrpStatsSysPtFragIpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 10),
    _JnxWxGrpStatsSysPtFragIpPkts_Type()
)
jnxWxGrpStatsSysPtFragIpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysPtFragIpPkts.setStatus("current")
_JnxWxGrpStatsSysPtVlanBytes_Type = Counter64
_JnxWxGrpStatsSysPtVlanBytes_Object = MibScalar
jnxWxGrpStatsSysPtVlanBytes = _JnxWxGrpStatsSysPtVlanBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 11),
    _JnxWxGrpStatsSysPtVlanBytes_Type()
)
jnxWxGrpStatsSysPtVlanBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysPtVlanBytes.setStatus("current")
_JnxWxGrpStatsSysPtVlanPkts_Type = Counter64
_JnxWxGrpStatsSysPtVlanPkts_Object = MibScalar
jnxWxGrpStatsSysPtVlanPkts = _JnxWxGrpStatsSysPtVlanPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 12),
    _JnxWxGrpStatsSysPtVlanPkts_Type()
)
jnxWxGrpStatsSysPtVlanPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysPtVlanPkts.setStatus("current")
_JnxWxGrpStatsSysPtMcastBytes_Type = Counter64
_JnxWxGrpStatsSysPtMcastBytes_Object = MibScalar
jnxWxGrpStatsSysPtMcastBytes = _JnxWxGrpStatsSysPtMcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 13),
    _JnxWxGrpStatsSysPtMcastBytes_Type()
)
jnxWxGrpStatsSysPtMcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysPtMcastBytes.setStatus("current")
_JnxWxGrpStatsSysPtMcastPkts_Type = Counter64
_JnxWxGrpStatsSysPtMcastPkts_Object = MibScalar
jnxWxGrpStatsSysPtMcastPkts = _JnxWxGrpStatsSysPtMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 14),
    _JnxWxGrpStatsSysPtMcastPkts_Type()
)
jnxWxGrpStatsSysPtMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysPtMcastPkts.setStatus("current")
_JnxWxGrpStatsSysComp_ObjectIdentity = ObjectIdentity
jnxWxGrpStatsSysComp = _JnxWxGrpStatsSysComp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysComp.setStatus("current")
_JnxWxGrpStatsSysCompFailAppDefDisableBytes_Type = Counter64
_JnxWxGrpStatsSysCompFailAppDefDisableBytes_Object = MibScalar
jnxWxGrpStatsSysCompFailAppDefDisableBytes = _JnxWxGrpStatsSysCompFailAppDefDisableBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2, 1),
    _JnxWxGrpStatsSysCompFailAppDefDisableBytes_Type()
)
jnxWxGrpStatsSysCompFailAppDefDisableBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysCompFailAppDefDisableBytes.setStatus("current")
_JnxWxGrpStatsSysCompFailAppDefDisablePkts_Type = Counter64
_JnxWxGrpStatsSysCompFailAppDefDisablePkts_Object = MibScalar
jnxWxGrpStatsSysCompFailAppDefDisablePkts = _JnxWxGrpStatsSysCompFailAppDefDisablePkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2, 2),
    _JnxWxGrpStatsSysCompFailAppDefDisablePkts_Type()
)
jnxWxGrpStatsSysCompFailAppDefDisablePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysCompFailAppDefDisablePkts.setStatus("current")
_JnxWxGrpStatsSysCompFailTcpAcclToRemoteBytes_Type = Counter64
_JnxWxGrpStatsSysCompFailTcpAcclToRemoteBytes_Object = MibScalar
jnxWxGrpStatsSysCompFailTcpAcclToRemoteBytes = _JnxWxGrpStatsSysCompFailTcpAcclToRemoteBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2, 3),
    _JnxWxGrpStatsSysCompFailTcpAcclToRemoteBytes_Type()
)
jnxWxGrpStatsSysCompFailTcpAcclToRemoteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysCompFailTcpAcclToRemoteBytes.setStatus("current")
_JnxWxGrpStatsSysCompFailTcpAcclToRemotePkts_Type = Counter64
_JnxWxGrpStatsSysCompFailTcpAcclToRemotePkts_Object = MibScalar
jnxWxGrpStatsSysCompFailTcpAcclToRemotePkts = _JnxWxGrpStatsSysCompFailTcpAcclToRemotePkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2, 4),
    _JnxWxGrpStatsSysCompFailTcpAcclToRemotePkts_Type()
)
jnxWxGrpStatsSysCompFailTcpAcclToRemotePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysCompFailTcpAcclToRemotePkts.setStatus("current")
_JnxWxGrpStatsSysCompFailResCrunchBytes_Type = Counter64
_JnxWxGrpStatsSysCompFailResCrunchBytes_Object = MibScalar
jnxWxGrpStatsSysCompFailResCrunchBytes = _JnxWxGrpStatsSysCompFailResCrunchBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2, 5),
    _JnxWxGrpStatsSysCompFailResCrunchBytes_Type()
)
jnxWxGrpStatsSysCompFailResCrunchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysCompFailResCrunchBytes.setStatus("current")
_JnxWxGrpStatsSysCompFailAlgoLimitBytes_Type = Counter64
_JnxWxGrpStatsSysCompFailAlgoLimitBytes_Object = MibScalar
jnxWxGrpStatsSysCompFailAlgoLimitBytes = _JnxWxGrpStatsSysCompFailAlgoLimitBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2, 6),
    _JnxWxGrpStatsSysCompFailAlgoLimitBytes_Type()
)
jnxWxGrpStatsSysCompFailAlgoLimitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysCompFailAlgoLimitBytes.setStatus("current")
_JnxWxGrpStatsSysCompTcpAcclFailedBytes_Type = Counter64
_JnxWxGrpStatsSysCompTcpAcclFailedBytes_Object = MibScalar
jnxWxGrpStatsSysCompTcpAcclFailedBytes = _JnxWxGrpStatsSysCompTcpAcclFailedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2, 7),
    _JnxWxGrpStatsSysCompTcpAcclFailedBytes_Type()
)
jnxWxGrpStatsSysCompTcpAcclFailedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysCompTcpAcclFailedBytes.setStatus("current")
_JnxWxGrpStatsSysCompTcpAcclFailedPkts_Type = Counter64
_JnxWxGrpStatsSysCompTcpAcclFailedPkts_Object = MibScalar
jnxWxGrpStatsSysCompTcpAcclFailedPkts = _JnxWxGrpStatsSysCompTcpAcclFailedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2, 8),
    _JnxWxGrpStatsSysCompTcpAcclFailedPkts_Type()
)
jnxWxGrpStatsSysCompTcpAcclFailedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysCompTcpAcclFailedPkts.setStatus("current")
_JnxWxGrpStatsSysCifs_ObjectIdentity = ObjectIdentity
jnxWxGrpStatsSysCifs = _JnxWxGrpStatsSysCifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysCifs.setStatus("current")
_JnxWxGrpStatsSysCifsFailAppDefBytes_Type = Counter64
_JnxWxGrpStatsSysCifsFailAppDefBytes_Object = MibScalar
jnxWxGrpStatsSysCifsFailAppDefBytes = _JnxWxGrpStatsSysCifsFailAppDefBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 3, 1),
    _JnxWxGrpStatsSysCifsFailAppDefBytes_Type()
)
jnxWxGrpStatsSysCifsFailAppDefBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysCifsFailAppDefBytes.setStatus("current")
_JnxWxGrpStatsSysCifsFailAppDefPkts_Type = Counter64
_JnxWxGrpStatsSysCifsFailAppDefPkts_Object = MibScalar
jnxWxGrpStatsSysCifsFailAppDefPkts = _JnxWxGrpStatsSysCifsFailAppDefPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 3, 2),
    _JnxWxGrpStatsSysCifsFailAppDefPkts_Type()
)
jnxWxGrpStatsSysCifsFailAppDefPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysCifsFailAppDefPkts.setStatus("current")
_JnxWxGrpStatsSysCifsFailTcpAcclToRemoteBytes_Type = Counter64
_JnxWxGrpStatsSysCifsFailTcpAcclToRemoteBytes_Object = MibScalar
jnxWxGrpStatsSysCifsFailTcpAcclToRemoteBytes = _JnxWxGrpStatsSysCifsFailTcpAcclToRemoteBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 3, 3),
    _JnxWxGrpStatsSysCifsFailTcpAcclToRemoteBytes_Type()
)
jnxWxGrpStatsSysCifsFailTcpAcclToRemoteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysCifsFailTcpAcclToRemoteBytes.setStatus("current")
_JnxWxGrpStatsSysCifsFailTcpAcclToRemotePkts_Type = Counter64
_JnxWxGrpStatsSysCifsFailTcpAcclToRemotePkts_Object = MibScalar
jnxWxGrpStatsSysCifsFailTcpAcclToRemotePkts = _JnxWxGrpStatsSysCifsFailTcpAcclToRemotePkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 3, 4),
    _JnxWxGrpStatsSysCifsFailTcpAcclToRemotePkts_Type()
)
jnxWxGrpStatsSysCifsFailTcpAcclToRemotePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysCifsFailTcpAcclToRemotePkts.setStatus("current")
_JnxWxGrpStatsSysCifsFailTcpAcclFailedBytes_Type = Counter64
_JnxWxGrpStatsSysCifsFailTcpAcclFailedBytes_Object = MibScalar
jnxWxGrpStatsSysCifsFailTcpAcclFailedBytes = _JnxWxGrpStatsSysCifsFailTcpAcclFailedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 3, 5),
    _JnxWxGrpStatsSysCifsFailTcpAcclFailedBytes_Type()
)
jnxWxGrpStatsSysCifsFailTcpAcclFailedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysCifsFailTcpAcclFailedBytes.setStatus("current")
_JnxWxGrpStatsSysCifsFailTcpAcclFailedPkts_Type = Counter64
_JnxWxGrpStatsSysCifsFailTcpAcclFailedPkts_Object = MibScalar
jnxWxGrpStatsSysCifsFailTcpAcclFailedPkts = _JnxWxGrpStatsSysCifsFailTcpAcclFailedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 3, 6),
    _JnxWxGrpStatsSysCifsFailTcpAcclFailedPkts_Type()
)
jnxWxGrpStatsSysCifsFailTcpAcclFailedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysCifsFailTcpAcclFailedPkts.setStatus("current")
_JnxWxGrpStatsSysExchange_ObjectIdentity = ObjectIdentity
jnxWxGrpStatsSysExchange = _JnxWxGrpStatsSysExchange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysExchange.setStatus("current")
_JnxWxGrpStatsSysExchangeFailAppDefBytes_Type = Counter64
_JnxWxGrpStatsSysExchangeFailAppDefBytes_Object = MibScalar
jnxWxGrpStatsSysExchangeFailAppDefBytes = _JnxWxGrpStatsSysExchangeFailAppDefBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 4, 1),
    _JnxWxGrpStatsSysExchangeFailAppDefBytes_Type()
)
jnxWxGrpStatsSysExchangeFailAppDefBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysExchangeFailAppDefBytes.setStatus("current")
_JnxWxGrpStatsSysExchangeFailAppDefPkts_Type = Counter64
_JnxWxGrpStatsSysExchangeFailAppDefPkts_Object = MibScalar
jnxWxGrpStatsSysExchangeFailAppDefPkts = _JnxWxGrpStatsSysExchangeFailAppDefPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 4, 2),
    _JnxWxGrpStatsSysExchangeFailAppDefPkts_Type()
)
jnxWxGrpStatsSysExchangeFailAppDefPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysExchangeFailAppDefPkts.setStatus("current")
_JnxWxGrpStatsSysExchangeFailTcpAcclToRemoteBytes_Type = Counter64
_JnxWxGrpStatsSysExchangeFailTcpAcclToRemoteBytes_Object = MibScalar
jnxWxGrpStatsSysExchangeFailTcpAcclToRemoteBytes = _JnxWxGrpStatsSysExchangeFailTcpAcclToRemoteBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 4, 3),
    _JnxWxGrpStatsSysExchangeFailTcpAcclToRemoteBytes_Type()
)
jnxWxGrpStatsSysExchangeFailTcpAcclToRemoteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysExchangeFailTcpAcclToRemoteBytes.setStatus("current")
_JnxWxGrpStatsSysExchangeFailTcpAcclToRemotePkts_Type = Counter64
_JnxWxGrpStatsSysExchangeFailTcpAcclToRemotePkts_Object = MibScalar
jnxWxGrpStatsSysExchangeFailTcpAcclToRemotePkts = _JnxWxGrpStatsSysExchangeFailTcpAcclToRemotePkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 4, 4),
    _JnxWxGrpStatsSysExchangeFailTcpAcclToRemotePkts_Type()
)
jnxWxGrpStatsSysExchangeFailTcpAcclToRemotePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysExchangeFailTcpAcclToRemotePkts.setStatus("current")
_JnxWxGrpStatsSysExchangeFailTcpAcclFailedBytes_Type = Counter64
_JnxWxGrpStatsSysExchangeFailTcpAcclFailedBytes_Object = MibScalar
jnxWxGrpStatsSysExchangeFailTcpAcclFailedBytes = _JnxWxGrpStatsSysExchangeFailTcpAcclFailedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 4, 5),
    _JnxWxGrpStatsSysExchangeFailTcpAcclFailedBytes_Type()
)
jnxWxGrpStatsSysExchangeFailTcpAcclFailedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysExchangeFailTcpAcclFailedBytes.setStatus("current")
_JnxWxGrpStatsSysExchangeFailTcpAcclFailedPkts_Type = Counter64
_JnxWxGrpStatsSysExchangeFailTcpAcclFailedPkts_Object = MibScalar
jnxWxGrpStatsSysExchangeFailTcpAcclFailedPkts = _JnxWxGrpStatsSysExchangeFailTcpAcclFailedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 4, 6),
    _JnxWxGrpStatsSysExchangeFailTcpAcclFailedPkts_Type()
)
jnxWxGrpStatsSysExchangeFailTcpAcclFailedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsSysExchangeFailTcpAcclFailedPkts.setStatus("current")
_JnxWxGrpStatsAccl_ObjectIdentity = ObjectIdentity
jnxWxGrpStatsAccl = _JnxWxGrpStatsAccl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    jnxWxGrpStatsAccl.setStatus("current")
_JnxWxGrpStatsTcpAcclTable_Object = MibTable
jnxWxGrpStatsTcpAcclTable = _JnxWxGrpStatsTcpAcclTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    jnxWxGrpStatsTcpAcclTable.setStatus("current")
_JnxWxGrpStatsTcpAcclEntry_Object = MibTableRow
jnxWxGrpStatsTcpAcclEntry = _JnxWxGrpStatsTcpAcclEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2, 1, 1)
)
jnxWxGrpStatsTcpAcclEntry.setIndexNames(
    (0, "JUNIPER-WX-STATUS-MIB", "jnxWxGrpStatusAppId"),
    (0, "JUNIPER-WX-STATUS-MIB", "jnxWxGrpStatusRemoteWxId"),
)
if mibBuilder.loadTexts:
    jnxWxGrpStatsTcpAcclEntry.setStatus("current")
_JnxWxGrpStatsTcpAcclPtFlows_Type = Counter32
_JnxWxGrpStatsTcpAcclPtFlows_Object = MibTableColumn
jnxWxGrpStatsTcpAcclPtFlows = _JnxWxGrpStatsTcpAcclPtFlows_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2, 1, 1, 1),
    _JnxWxGrpStatsTcpAcclPtFlows_Type()
)
jnxWxGrpStatsTcpAcclPtFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsTcpAcclPtFlows.setStatus("current")
_JnxWxGrpStatsTcpAcclProxyFlows_Type = Counter32
_JnxWxGrpStatsTcpAcclProxyFlows_Object = MibTableColumn
jnxWxGrpStatsTcpAcclProxyFlows = _JnxWxGrpStatsTcpAcclProxyFlows_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2, 1, 1, 2),
    _JnxWxGrpStatsTcpAcclProxyFlows_Type()
)
jnxWxGrpStatsTcpAcclProxyFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsTcpAcclProxyFlows.setStatus("current")
_JnxWxGrpStatsTcpAcclPtFlowsDiff_Type = Counter32
_JnxWxGrpStatsTcpAcclPtFlowsDiff_Object = MibTableColumn
jnxWxGrpStatsTcpAcclPtFlowsDiff = _JnxWxGrpStatsTcpAcclPtFlowsDiff_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2, 1, 1, 3),
    _JnxWxGrpStatsTcpAcclPtFlowsDiff_Type()
)
jnxWxGrpStatsTcpAcclPtFlowsDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsTcpAcclPtFlowsDiff.setStatus("current")
_JnxWxGrpStatsTcpAcclProxyRequestsDiff_Type = Counter32
_JnxWxGrpStatsTcpAcclProxyRequestsDiff_Object = MibTableColumn
jnxWxGrpStatsTcpAcclProxyRequestsDiff = _JnxWxGrpStatsTcpAcclProxyRequestsDiff_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2, 1, 1, 4),
    _JnxWxGrpStatsTcpAcclProxyRequestsDiff_Type()
)
jnxWxGrpStatsTcpAcclProxyRequestsDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsTcpAcclProxyRequestsDiff.setStatus("current")
_JnxWxGrpStatsTcpAcclProxyFlowsDiff_Type = Counter32
_JnxWxGrpStatsTcpAcclProxyFlowsDiff_Object = MibTableColumn
jnxWxGrpStatsTcpAcclProxyFlowsDiff = _JnxWxGrpStatsTcpAcclProxyFlowsDiff_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2, 1, 1, 5),
    _JnxWxGrpStatsTcpAcclProxyFlowsDiff_Type()
)
jnxWxGrpStatsTcpAcclProxyFlowsDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsTcpAcclProxyFlowsDiff.setStatus("current")
_JnxWxGrpStatsTcpAcclFailedToProxyDiff_Type = Counter32
_JnxWxGrpStatsTcpAcclFailedToProxyDiff_Object = MibTableColumn
jnxWxGrpStatsTcpAcclFailedToProxyDiff = _JnxWxGrpStatsTcpAcclFailedToProxyDiff_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2, 1, 1, 6),
    _JnxWxGrpStatsTcpAcclFailedToProxyDiff_Type()
)
jnxWxGrpStatsTcpAcclFailedToProxyDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsTcpAcclFailedToProxyDiff.setStatus("current")
_JnxWxGrpStatsComp_ObjectIdentity = ObjectIdentity
jnxWxGrpStatsComp = _JnxWxGrpStatsComp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    jnxWxGrpStatsComp.setStatus("current")
_JnxWxGrpStatsCompTable_Object = MibTable
jnxWxGrpStatsCompTable = _JnxWxGrpStatsCompTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    jnxWxGrpStatsCompTable.setStatus("current")
_JnxWxGrpStatsCompEntry_Object = MibTableRow
jnxWxGrpStatsCompEntry = _JnxWxGrpStatsCompEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 3, 1, 1)
)
jnxWxGrpStatsCompEntry.setIndexNames(
    (0, "JUNIPER-WX-STATUS-MIB", "jnxWxGrpStatusAppId"),
    (0, "JUNIPER-WX-STATUS-MIB", "jnxWxGrpStatusRemoteWxId"),
)
if mibBuilder.loadTexts:
    jnxWxGrpStatsCompEntry.setStatus("current")
_JnxWxGrpStatsCompBytesIn_Type = Counter64
_JnxWxGrpStatsCompBytesIn_Object = MibTableColumn
jnxWxGrpStatsCompBytesIn = _JnxWxGrpStatsCompBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 3, 1, 1, 1),
    _JnxWxGrpStatsCompBytesIn_Type()
)
jnxWxGrpStatsCompBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsCompBytesIn.setStatus("current")
_JnxWxGrpStatsCompBytesOut_Type = Counter64
_JnxWxGrpStatsCompBytesOut_Object = MibTableColumn
jnxWxGrpStatsCompBytesOut = _JnxWxGrpStatsCompBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 3, 1, 1, 2),
    _JnxWxGrpStatsCompBytesOut_Type()
)
jnxWxGrpStatsCompBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsCompBytesOut.setStatus("current")
_JnxWxGrpStatsCompCacheHits_Type = Counter64
_JnxWxGrpStatsCompCacheHits_Object = MibTableColumn
jnxWxGrpStatsCompCacheHits = _JnxWxGrpStatsCompCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 3, 1, 1, 3),
    _JnxWxGrpStatsCompCacheHits_Type()
)
jnxWxGrpStatsCompCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsCompCacheHits.setStatus("current")
_JnxWxGrpStatsCompCacheMisses_Type = Counter64
_JnxWxGrpStatsCompCacheMisses_Object = MibTableColumn
jnxWxGrpStatsCompCacheMisses = _JnxWxGrpStatsCompCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 3, 1, 1, 4),
    _JnxWxGrpStatsCompCacheMisses_Type()
)
jnxWxGrpStatsCompCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsCompCacheMisses.setStatus("current")
_JnxWxGrpStatsWanPerf_ObjectIdentity = ObjectIdentity
jnxWxGrpStatsWanPerf = _JnxWxGrpStatsWanPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    jnxWxGrpStatsWanPerf.setStatus("current")
_JnxWxGrpStatsWanPerfTable_Object = MibTable
jnxWxGrpStatsWanPerfTable = _JnxWxGrpStatsWanPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    jnxWxGrpStatsWanPerfTable.setStatus("current")
_JnxWxGrpStatsWanPerfEntry_Object = MibTableRow
jnxWxGrpStatsWanPerfEntry = _JnxWxGrpStatsWanPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 4, 1, 1)
)
jnxWxGrpStatsWanPerfEntry.setIndexNames(
    (0, "JUNIPER-WX-STATUS-MIB", "jnxWxGrpStatusAppId"),
    (0, "JUNIPER-WX-STATUS-MIB", "jnxWxGrpStatusRemoteWxId"),
)
if mibBuilder.loadTexts:
    jnxWxGrpStatsWanPerfEntry.setStatus("current")
_JnxWxGrpStatsWanPerfBytesToWan_Type = Counter64
_JnxWxGrpStatsWanPerfBytesToWan_Object = MibTableColumn
jnxWxGrpStatsWanPerfBytesToWan = _JnxWxGrpStatsWanPerfBytesToWan_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 4, 1, 1, 1),
    _JnxWxGrpStatsWanPerfBytesToWan_Type()
)
jnxWxGrpStatsWanPerfBytesToWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsWanPerfBytesToWan.setStatus("current")
_JnxWxGrpStatsWanPerfBytesFromWan_Type = Counter64
_JnxWxGrpStatsWanPerfBytesFromWan_Object = MibTableColumn
jnxWxGrpStatsWanPerfBytesFromWan = _JnxWxGrpStatsWanPerfBytesFromWan_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 4, 1, 1, 2),
    _JnxWxGrpStatsWanPerfBytesFromWan_Type()
)
jnxWxGrpStatsWanPerfBytesFromWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxGrpStatsWanPerfBytesFromWan.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-WX-STATS-MIB",
    **{"jnxWxGrpStatsSys": jnxWxGrpStatsSys,
       "jnxWxGrpStatsSysPt": jnxWxGrpStatsSysPt,
       "jnxWxGrpStatsSysPtAppDefMatchBytes": jnxWxGrpStatsSysPtAppDefMatchBytes,
       "jnxWxGrpStatsSysPtAppDefMatchPkts": jnxWxGrpStatsSysPtAppDefMatchPkts,
       "jnxWxGrpStatsSysPtNoRemoteWxBytes": jnxWxGrpStatsSysPtNoRemoteWxBytes,
       "jnxWxGrpStatsSysPtNoRemoteWxPkts": jnxWxGrpStatsSysPtNoRemoteWxPkts,
       "jnxWxGrpStatsSysPtNonTcpProtoBytes": jnxWxGrpStatsSysPtNonTcpProtoBytes,
       "jnxWxGrpStatsSysPtNonTcpProtoPkts": jnxWxGrpStatsSysPtNonTcpProtoPkts,
       "jnxWxGrpStatsSysPtNonIpBytes": jnxWxGrpStatsSysPtNonIpBytes,
       "jnxWxGrpStatsSysPtNonIpPkts": jnxWxGrpStatsSysPtNonIpPkts,
       "jnxWxGrpStatsSysPtFragIpBytes": jnxWxGrpStatsSysPtFragIpBytes,
       "jnxWxGrpStatsSysPtFragIpPkts": jnxWxGrpStatsSysPtFragIpPkts,
       "jnxWxGrpStatsSysPtVlanBytes": jnxWxGrpStatsSysPtVlanBytes,
       "jnxWxGrpStatsSysPtVlanPkts": jnxWxGrpStatsSysPtVlanPkts,
       "jnxWxGrpStatsSysPtMcastBytes": jnxWxGrpStatsSysPtMcastBytes,
       "jnxWxGrpStatsSysPtMcastPkts": jnxWxGrpStatsSysPtMcastPkts,
       "jnxWxGrpStatsSysComp": jnxWxGrpStatsSysComp,
       "jnxWxGrpStatsSysCompFailAppDefDisableBytes": jnxWxGrpStatsSysCompFailAppDefDisableBytes,
       "jnxWxGrpStatsSysCompFailAppDefDisablePkts": jnxWxGrpStatsSysCompFailAppDefDisablePkts,
       "jnxWxGrpStatsSysCompFailTcpAcclToRemoteBytes": jnxWxGrpStatsSysCompFailTcpAcclToRemoteBytes,
       "jnxWxGrpStatsSysCompFailTcpAcclToRemotePkts": jnxWxGrpStatsSysCompFailTcpAcclToRemotePkts,
       "jnxWxGrpStatsSysCompFailResCrunchBytes": jnxWxGrpStatsSysCompFailResCrunchBytes,
       "jnxWxGrpStatsSysCompFailAlgoLimitBytes": jnxWxGrpStatsSysCompFailAlgoLimitBytes,
       "jnxWxGrpStatsSysCompTcpAcclFailedBytes": jnxWxGrpStatsSysCompTcpAcclFailedBytes,
       "jnxWxGrpStatsSysCompTcpAcclFailedPkts": jnxWxGrpStatsSysCompTcpAcclFailedPkts,
       "jnxWxGrpStatsSysCifs": jnxWxGrpStatsSysCifs,
       "jnxWxGrpStatsSysCifsFailAppDefBytes": jnxWxGrpStatsSysCifsFailAppDefBytes,
       "jnxWxGrpStatsSysCifsFailAppDefPkts": jnxWxGrpStatsSysCifsFailAppDefPkts,
       "jnxWxGrpStatsSysCifsFailTcpAcclToRemoteBytes": jnxWxGrpStatsSysCifsFailTcpAcclToRemoteBytes,
       "jnxWxGrpStatsSysCifsFailTcpAcclToRemotePkts": jnxWxGrpStatsSysCifsFailTcpAcclToRemotePkts,
       "jnxWxGrpStatsSysCifsFailTcpAcclFailedBytes": jnxWxGrpStatsSysCifsFailTcpAcclFailedBytes,
       "jnxWxGrpStatsSysCifsFailTcpAcclFailedPkts": jnxWxGrpStatsSysCifsFailTcpAcclFailedPkts,
       "jnxWxGrpStatsSysExchange": jnxWxGrpStatsSysExchange,
       "jnxWxGrpStatsSysExchangeFailAppDefBytes": jnxWxGrpStatsSysExchangeFailAppDefBytes,
       "jnxWxGrpStatsSysExchangeFailAppDefPkts": jnxWxGrpStatsSysExchangeFailAppDefPkts,
       "jnxWxGrpStatsSysExchangeFailTcpAcclToRemoteBytes": jnxWxGrpStatsSysExchangeFailTcpAcclToRemoteBytes,
       "jnxWxGrpStatsSysExchangeFailTcpAcclToRemotePkts": jnxWxGrpStatsSysExchangeFailTcpAcclToRemotePkts,
       "jnxWxGrpStatsSysExchangeFailTcpAcclFailedBytes": jnxWxGrpStatsSysExchangeFailTcpAcclFailedBytes,
       "jnxWxGrpStatsSysExchangeFailTcpAcclFailedPkts": jnxWxGrpStatsSysExchangeFailTcpAcclFailedPkts,
       "jnxWxGrpStatsAccl": jnxWxGrpStatsAccl,
       "jnxWxGrpStatsTcpAcclTable": jnxWxGrpStatsTcpAcclTable,
       "jnxWxGrpStatsTcpAcclEntry": jnxWxGrpStatsTcpAcclEntry,
       "jnxWxGrpStatsTcpAcclPtFlows": jnxWxGrpStatsTcpAcclPtFlows,
       "jnxWxGrpStatsTcpAcclProxyFlows": jnxWxGrpStatsTcpAcclProxyFlows,
       "jnxWxGrpStatsTcpAcclPtFlowsDiff": jnxWxGrpStatsTcpAcclPtFlowsDiff,
       "jnxWxGrpStatsTcpAcclProxyRequestsDiff": jnxWxGrpStatsTcpAcclProxyRequestsDiff,
       "jnxWxGrpStatsTcpAcclProxyFlowsDiff": jnxWxGrpStatsTcpAcclProxyFlowsDiff,
       "jnxWxGrpStatsTcpAcclFailedToProxyDiff": jnxWxGrpStatsTcpAcclFailedToProxyDiff,
       "jnxWxGrpStatsComp": jnxWxGrpStatsComp,
       "jnxWxGrpStatsCompTable": jnxWxGrpStatsCompTable,
       "jnxWxGrpStatsCompEntry": jnxWxGrpStatsCompEntry,
       "jnxWxGrpStatsCompBytesIn": jnxWxGrpStatsCompBytesIn,
       "jnxWxGrpStatsCompBytesOut": jnxWxGrpStatsCompBytesOut,
       "jnxWxGrpStatsCompCacheHits": jnxWxGrpStatsCompCacheHits,
       "jnxWxGrpStatsCompCacheMisses": jnxWxGrpStatsCompCacheMisses,
       "jnxWxGrpStatsWanPerf": jnxWxGrpStatsWanPerf,
       "jnxWxGrpStatsWanPerfTable": jnxWxGrpStatsWanPerfTable,
       "jnxWxGrpStatsWanPerfEntry": jnxWxGrpStatsWanPerfEntry,
       "jnxWxGrpStatsWanPerfBytesToWan": jnxWxGrpStatsWanPerfBytesToWan,
       "jnxWxGrpStatsWanPerfBytesFromWan": jnxWxGrpStatsWanPerfBytesFromWan}
)
