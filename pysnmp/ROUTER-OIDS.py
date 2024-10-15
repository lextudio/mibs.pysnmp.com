# SNMP MIB module (ROUTER-OIDS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ROUTER-OIDS
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:32 2024
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

(ctNetwork,
 ctronExp) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctNetwork",
    "ctronExp")

(networkType,) = mibBuilder.importSymbols(
    "CTRON-OIDS",
    "networkType")

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

_NtProtoSuites_ObjectIdentity = ObjectIdentity
ntProtoSuites = _NtProtoSuites_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1)
)
_NtIpRouter_ObjectIdentity = ObjectIdentity
ntIpRouter = _NtIpRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1)
)
_NtIpRip_ObjectIdentity = ObjectIdentity
ntIpRip = _NtIpRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 1)
)
_NtIpOspf_ObjectIdentity = ObjectIdentity
ntIpOspf = _NtIpOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 2)
)
_NtIpFib_ObjectIdentity = ObjectIdentity
ntIpFib = _NtIpFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 3)
)
_NtIpArp_ObjectIdentity = ObjectIdentity
ntIpArp = _NtIpArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 4)
)
_NtIpAc1_ObjectIdentity = ObjectIdentity
ntIpAc1 = _NtIpAc1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 5)
)
_NtIpFwdEng_ObjectIdentity = ObjectIdentity
ntIpFwdEng = _NtIpFwdEng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 6)
)
_NtIpPortRedirect_ObjectIdentity = ObjectIdentity
ntIpPortRedirect = _NtIpPortRedirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 7)
)
_NtIpEventLog_ObjectIdentity = ObjectIdentity
ntIpEventLog = _NtIpEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 8)
)
_NtIpAddressTable_ObjectIdentity = ObjectIdentity
ntIpAddressTable = _NtIpAddressTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 9)
)
_NtIpxRouter_ObjectIdentity = ObjectIdentity
ntIpxRouter = _NtIpxRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2)
)
_NtIpxRip_ObjectIdentity = ObjectIdentity
ntIpxRip = _NtIpxRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 1)
)
_NtIpxSap_ObjectIdentity = ObjectIdentity
ntIpxSap = _NtIpxSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 2)
)
_NtIpxFib_ObjectIdentity = ObjectIdentity
ntIpxFib = _NtIpxFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 3)
)
_NtIpxAc1_ObjectIdentity = ObjectIdentity
ntIpxAc1 = _NtIpxAc1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 5)
)
_NtIpxFwdEng_ObjectIdentity = ObjectIdentity
ntIpxFwdEng = _NtIpxFwdEng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 6)
)
_NtIpxPortRedirect_ObjectIdentity = ObjectIdentity
ntIpxPortRedirect = _NtIpxPortRedirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 7)
)
_NtIpxEventLog_ObjectIdentity = ObjectIdentity
ntIpxEventLog = _NtIpxEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 8)
)
_NtIpxAddressTable_ObjectIdentity = ObjectIdentity
ntIpxAddressTable = _NtIpxAddressTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 9)
)
_NtIpxEcho_ObjectIdentity = ObjectIdentity
ntIpxEcho = _NtIpxEcho_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 10)
)
_NtIpxBroadcast_ObjectIdentity = ObjectIdentity
ntIpxBroadcast = _NtIpxBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 11)
)
_NtIpxNetbios_ObjectIdentity = ObjectIdentity
ntIpxNetbios = _NtIpxNetbios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 12)
)
_NtDecIVRouter_ObjectIdentity = ObjectIdentity
ntDecIVRouter = _NtDecIVRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3)
)
_NtDecIVLevel1_ObjectIdentity = ObjectIdentity
ntDecIVLevel1 = _NtDecIVLevel1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 1)
)
_NtDecIVLevel2_ObjectIdentity = ObjectIdentity
ntDecIVLevel2 = _NtDecIVLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 2)
)
_NtDecIVFib_ObjectIdentity = ObjectIdentity
ntDecIVFib = _NtDecIVFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 3)
)
_NtDecIVAcl_ObjectIdentity = ObjectIdentity
ntDecIVAcl = _NtDecIVAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 5)
)
_NtDecIVFwdEng_ObjectIdentity = ObjectIdentity
ntDecIVFwdEng = _NtDecIVFwdEng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 6)
)
_NtDecIVPportRedirect_ObjectIdentity = ObjectIdentity
ntDecIVPportRedirect = _NtDecIVPportRedirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 7)
)
_NtDecIVEventLog_ObjectIdentity = ObjectIdentity
ntDecIVEventLog = _NtDecIVEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 8)
)
_NtDecIVAddressTable_ObjectIdentity = ObjectIdentity
ntDecIVAddressTable = _NtDecIVAddressTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 9)
)
_NtAtRouter_ObjectIdentity = ObjectIdentity
ntAtRouter = _NtAtRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4)
)
_NtAtRtgProt_ObjectIdentity = ObjectIdentity
ntAtRtgProt = _NtAtRtgProt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 1)
)
_NtAtFib_ObjectIdentity = ObjectIdentity
ntAtFib = _NtAtFib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 3)
)
_NtAtArp_ObjectIdentity = ObjectIdentity
ntAtArp = _NtAtArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 4)
)
_NtAtAcl_ObjectIdentity = ObjectIdentity
ntAtAcl = _NtAtAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 5)
)
_NtAtFwdEng_ObjectIdentity = ObjectIdentity
ntAtFwdEng = _NtAtFwdEng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 6)
)
_NtAtEventLog_ObjectIdentity = ObjectIdentity
ntAtEventLog = _NtAtEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 8)
)
_NtAtAddressTable_ObjectIdentity = ObjectIdentity
ntAtAddressTable = _NtAtAddressTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 9)
)
_NtAppnRouter_ObjectIdentity = ObjectIdentity
ntAppnRouter = _NtAppnRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 5)
)
_NtAppnFwdEng_ObjectIdentity = ObjectIdentity
ntAppnFwdEng = _NtAppnFwdEng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 5, 6)
)
_NtAppnEventLog_ObjectIdentity = ObjectIdentity
ntAppnEventLog = _NtAppnEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 5, 8)
)
_NtAppnExtensionTable_ObjectIdentity = ObjectIdentity
ntAppnExtensionTable = _NtAppnExtensionTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 5, 9)
)
_NtAppnIsr_ObjectIdentity = ObjectIdentity
ntAppnIsr = _NtAppnIsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 5, 10)
)
_CtRouter_ObjectIdentity = ObjectIdentity
ctRouter = _CtRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2)
)
_CtHighLevelView_ObjectIdentity = ObjectIdentity
ctHighLevelView = _CtHighLevelView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 2)
)
_CtApplicationView_ObjectIdentity = ObjectIdentity
ctApplicationView = _CtApplicationView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 2, 1)
)
_CtProtoSuites_ObjectIdentity = ObjectIdentity
ctProtoSuites = _CtProtoSuites_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3)
)
_CtIpRouter_ObjectIdentity = ObjectIdentity
ctIpRouter = _CtIpRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3, 1)
)
_CtIpxRouter_ObjectIdentity = ObjectIdentity
ctIpxRouter = _CtIpxRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3, 2)
)
_CtDecIVRouter_ObjectIdentity = ObjectIdentity
ctDecIVRouter = _CtDecIVRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3, 3)
)
_CtAtRouter_ObjectIdentity = ObjectIdentity
ctAtRouter = _CtAtRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3, 4)
)
_CtAppnRouter_ObjectIdentity = ObjectIdentity
ctAppnRouter = _CtAppnRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3, 5)
)
_CtronRouterExp_ObjectIdentity = ObjectIdentity
ctronRouterExp = _CtronRouterExp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2)
)
_NwRouter_ObjectIdentity = ObjectIdentity
nwRouter = _NwRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2)
)
_NwRtrMibs_ObjectIdentity = ObjectIdentity
nwRtrMibs = _NwRtrMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 1)
)
_NwRtrHighLevelView_ObjectIdentity = ObjectIdentity
nwRtrHighLevelView = _NwRtrHighLevelView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2)
)
_NwRtrProtoSuites_ObjectIdentity = ObjectIdentity
nwRtrProtoSuites = _NwRtrProtoSuites_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROUTER-OIDS",
    **{"ntProtoSuites": ntProtoSuites,
       "ntIpRouter": ntIpRouter,
       "ntIpRip": ntIpRip,
       "ntIpOspf": ntIpOspf,
       "ntIpFib": ntIpFib,
       "ntIpArp": ntIpArp,
       "ntIpAc1": ntIpAc1,
       "ntIpFwdEng": ntIpFwdEng,
       "ntIpPortRedirect": ntIpPortRedirect,
       "ntIpEventLog": ntIpEventLog,
       "ntIpAddressTable": ntIpAddressTable,
       "ntIpxRouter": ntIpxRouter,
       "ntIpxRip": ntIpxRip,
       "ntIpxSap": ntIpxSap,
       "ntIpxFib": ntIpxFib,
       "ntIpxAc1": ntIpxAc1,
       "ntIpxFwdEng": ntIpxFwdEng,
       "ntIpxPortRedirect": ntIpxPortRedirect,
       "ntIpxEventLog": ntIpxEventLog,
       "ntIpxAddressTable": ntIpxAddressTable,
       "ntIpxEcho": ntIpxEcho,
       "ntIpxBroadcast": ntIpxBroadcast,
       "ntIpxNetbios": ntIpxNetbios,
       "ntDecIVRouter": ntDecIVRouter,
       "ntDecIVLevel1": ntDecIVLevel1,
       "ntDecIVLevel2": ntDecIVLevel2,
       "ntDecIVFib": ntDecIVFib,
       "ntDecIVAcl": ntDecIVAcl,
       "ntDecIVFwdEng": ntDecIVFwdEng,
       "ntDecIVPportRedirect": ntDecIVPportRedirect,
       "ntDecIVEventLog": ntDecIVEventLog,
       "ntDecIVAddressTable": ntDecIVAddressTable,
       "ntAtRouter": ntAtRouter,
       "ntAtRtgProt": ntAtRtgProt,
       "ntAtFib": ntAtFib,
       "ntAtArp": ntAtArp,
       "ntAtAcl": ntAtAcl,
       "ntAtFwdEng": ntAtFwdEng,
       "ntAtEventLog": ntAtEventLog,
       "ntAtAddressTable": ntAtAddressTable,
       "ntAppnRouter": ntAppnRouter,
       "ntAppnFwdEng": ntAppnFwdEng,
       "ntAppnEventLog": ntAppnEventLog,
       "ntAppnExtensionTable": ntAppnExtensionTable,
       "ntAppnIsr": ntAppnIsr,
       "ctRouter": ctRouter,
       "ctHighLevelView": ctHighLevelView,
       "ctApplicationView": ctApplicationView,
       "ctProtoSuites": ctProtoSuites,
       "ctIpRouter": ctIpRouter,
       "ctIpxRouter": ctIpxRouter,
       "ctDecIVRouter": ctDecIVRouter,
       "ctAtRouter": ctAtRouter,
       "ctAppnRouter": ctAppnRouter,
       "ctronRouterExp": ctronRouterExp,
       "nwRouter": nwRouter,
       "nwRtrMibs": nwRtrMibs,
       "nwRtrHighLevelView": nwRtrHighLevelView,
       "nwRtrProtoSuites": nwRtrProtoSuites}
)
