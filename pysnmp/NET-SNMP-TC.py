# SNMP MIB module (NET-SNMP-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NET-SNMP-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:25 2024
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

(netSnmpAgentOIDs,
 netSnmpDomains,
 netSnmpModuleIDs) = mibBuilder.importSymbols(
    "NET-SNMP-MIB",
    "netSnmpAgentOIDs",
    "netSnmpDomains",
    "netSnmpModuleIDs")

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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

netSnmpTCs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 1)
)
netSnmpTCs.setRevisions(
        ("2002-02-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Float(Opaque, TextualConvention):
    status = "current"
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )



# MIB Managed Objects in the order of their OIDs

_Hpux9_ObjectIdentity = ObjectIdentity
hpux9 = _Hpux9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 1)
)
_Sunos4_ObjectIdentity = ObjectIdentity
sunos4 = _Sunos4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 2)
)
_Solaris_ObjectIdentity = ObjectIdentity
solaris = _Solaris_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 3)
)
_Osf_ObjectIdentity = ObjectIdentity
osf = _Osf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 4)
)
_Ultrix_ObjectIdentity = ObjectIdentity
ultrix = _Ultrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 5)
)
_Hpux10_ObjectIdentity = ObjectIdentity
hpux10 = _Hpux10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 6)
)
_Netbsd_ObjectIdentity = ObjectIdentity
netbsd = _Netbsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 7)
)
_Freebsd_ObjectIdentity = ObjectIdentity
freebsd = _Freebsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 8)
)
_Irix_ObjectIdentity = ObjectIdentity
irix = _Irix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 9)
)
_Linux_ObjectIdentity = ObjectIdentity
linux = _Linux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 10)
)
_Bsdi_ObjectIdentity = ObjectIdentity
bsdi = _Bsdi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 11)
)
_Openbsd_ObjectIdentity = ObjectIdentity
openbsd = _Openbsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 12)
)
_Win32_ObjectIdentity = ObjectIdentity
win32 = _Win32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 13)
)
_Hpux11_ObjectIdentity = ObjectIdentity
hpux11 = _Hpux11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 14)
)
_Aix_ObjectIdentity = ObjectIdentity
aix = _Aix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 15)
)
_Macosx_ObjectIdentity = ObjectIdentity
macosx = _Macosx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 16)
)
_Dragonfly_ObjectIdentity = ObjectIdentity
dragonfly = _Dragonfly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 17)
)
_Unknown_ObjectIdentity = ObjectIdentity
unknown = _Unknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 2, 255)
)
_NetSnmpTCPDomain_ObjectIdentity = ObjectIdentity
netSnmpTCPDomain = _NetSnmpTCPDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 3, 1)
)
_NetSnmpUnixDomain_ObjectIdentity = ObjectIdentity
netSnmpUnixDomain = _NetSnmpUnixDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 3, 2)
)
_NetSnmpAAL5PVCDomain_ObjectIdentity = ObjectIdentity
netSnmpAAL5PVCDomain = _NetSnmpAAL5PVCDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 3, 3)
)
_NetSnmpUDPIPv6Domain_ObjectIdentity = ObjectIdentity
netSnmpUDPIPv6Domain = _NetSnmpUDPIPv6Domain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 3, 4)
)
_NetSnmpTCPIPv6Domain_ObjectIdentity = ObjectIdentity
netSnmpTCPIPv6Domain = _NetSnmpTCPIPv6Domain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 3, 5)
)
_NetSnmpCallbackDomain_ObjectIdentity = ObjectIdentity
netSnmpCallbackDomain = _NetSnmpCallbackDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 3, 6)
)
_NetSnmpAliasDomain_ObjectIdentity = ObjectIdentity
netSnmpAliasDomain = _NetSnmpAliasDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 3, 7)
)
_NetSnmpDTLSUDPDomain_ObjectIdentity = ObjectIdentity
netSnmpDTLSUDPDomain = _NetSnmpDTLSUDPDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 3, 8)
)
_NetSnmpDTLSSCTPDomain_ObjectIdentity = ObjectIdentity
netSnmpDTLSSCTPDomain = _NetSnmpDTLSSCTPDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 3, 9)
)
_NetSnmpTLSTCPDomain_ObjectIdentity = ObjectIdentity
netSnmpTLSTCPDomain = _NetSnmpTLSTCPDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 3, 10)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NET-SNMP-TC",
    **{"Float": Float,
       "netSnmpTCs": netSnmpTCs,
       "hpux9": hpux9,
       "sunos4": sunos4,
       "solaris": solaris,
       "osf": osf,
       "ultrix": ultrix,
       "hpux10": hpux10,
       "netbsd": netbsd,
       "freebsd": freebsd,
       "irix": irix,
       "linux": linux,
       "bsdi": bsdi,
       "openbsd": openbsd,
       "win32": win32,
       "hpux11": hpux11,
       "aix": aix,
       "macosx": macosx,
       "dragonfly": dragonfly,
       "unknown": unknown,
       "netSnmpTCPDomain": netSnmpTCPDomain,
       "netSnmpUnixDomain": netSnmpUnixDomain,
       "netSnmpAAL5PVCDomain": netSnmpAAL5PVCDomain,
       "netSnmpUDPIPv6Domain": netSnmpUDPIPv6Domain,
       "netSnmpTCPIPv6Domain": netSnmpTCPIPv6Domain,
       "netSnmpCallbackDomain": netSnmpCallbackDomain,
       "netSnmpAliasDomain": netSnmpAliasDomain,
       "netSnmpDTLSUDPDomain": netSnmpDTLSUDPDomain,
       "netSnmpDTLSSCTPDomain": netSnmpDTLSSCTPDomain,
       "netSnmpTLSTCPDomain": netSnmpTLSTCPDomain}
)
