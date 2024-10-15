# SNMP MIB module (XYLO-MIB-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLO-MIB-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:31 2024
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
 enterprises,
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
    "enterprises",
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

_Xylogics_ObjectIdentity = ObjectIdentity
xylogics = _Xylogics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15)
)
_Prod_ObjectIdentity = ObjectIdentity
prod = _Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1)
)


class _Prodannex_Type(DisplayString):
    """Custom type prodannex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Prodannex_Type.__name__ = "DisplayString"
_Prodannex_Object = MibScalar
prodannex = _Prodannex_Object(
    (1, 3, 6, 1, 4, 1, 15, 1, 1),
    _Prodannex_Type()
)
prodannex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodannex.setStatus("mandatory")


class _Mibversion_Type(DisplayString):
    """Custom type mibversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Mibversion_Type.__name__ = "DisplayString"
_Mibversion_Object = MibScalar
mibversion = _Mibversion_Object(
    (1, 3, 6, 1, 4, 1, 15, 1, 2),
    _Mibversion_Type()
)
mibversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibversion.setStatus("mandatory")
_Prodoid_ObjectIdentity = ObjectIdentity
prodoid = _Prodoid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3)
)
_Unknown_ObjectIdentity = ObjectIdentity
unknown = _Unknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 1)
)
_AnnexII_ObjectIdentity = ObjectIdentity
annexII = _AnnexII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 2)
)
_Annex3_ObjectIdentity = ObjectIdentity
annex3 = _Annex3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 3)
)
_Microanx_ObjectIdentity = ObjectIdentity
microanx = _Microanx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 4)
)
_Microels_ObjectIdentity = ObjectIdentity
microels = _Microels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 5)
)
_Csmim1_ObjectIdentity = ObjectIdentity
csmim1 = _Csmim1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 6)
)
_Ods_ObjectIdentity = ObjectIdentity
ods = _Ods_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 7)
)
_Bay5390_ObjectIdentity = ObjectIdentity
bay5390 = _Bay5390_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 8)
)
_Csmim2_ObjectIdentity = ObjectIdentity
csmim2 = _Csmim2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 9)
)
_Annex2000_ObjectIdentity = ObjectIdentity
annex2000 = _Annex2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 10)
)
_Microcs_ObjectIdentity = ObjectIdentity
microcs = _Microcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 11)
)
_Annex4000_ObjectIdentity = ObjectIdentity
annex4000 = _Annex4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 12)
)
_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 13)
)
_Csmim_t1_ObjectIdentity = ObjectIdentity
csmim_t1 = _Csmim_t1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 14)
)
_Ra6100_ObjectIdentity = ObjectIdentity
ra6100 = _Ra6100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 15)
)
_Ra6300_ObjectIdentity = ObjectIdentity
ra6300 = _Ra6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 16)
)
_Bay5391_ObjectIdentity = ObjectIdentity
bay5391 = _Bay5391_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 17)
)
_Bay5393_ObjectIdentity = ObjectIdentity
bay5393 = _Bay5393_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 18)
)
_Bay5399_ObjectIdentity = ObjectIdentity
bay5399 = _Bay5399_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1, 3, 19)
)
_Annex_ObjectIdentity = ObjectIdentity
annex = _Annex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2)
)
_Hw_ObjectIdentity = ObjectIdentity
hw = _Hw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 1)
)
_Sw_ObjectIdentity = ObjectIdentity
sw = _Sw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 2)
)
_Ports_ObjectIdentity = ObjectIdentity
ports = _Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 3)
)
_Parallelport_ObjectIdentity = ObjectIdentity
parallelport = _Parallelport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 4)
)
_Annexconfig_ObjectIdentity = ObjectIdentity
annexconfig = _Annexconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 5)
)
_Anxigmpconfig_ObjectIdentity = ObjectIdentity
anxigmpconfig = _Anxigmpconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 105)
)
_Annexcmds_ObjectIdentity = ObjectIdentity
annexcmds = _Annexcmds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 6)
)
_Annexlatstats_ObjectIdentity = ObjectIdentity
annexlatstats = _Annexlatstats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 7)
)
_Interfacerip_ObjectIdentity = ObjectIdentity
interfacerip = _Interfacerip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 8)
)
_Anxsyncports_ObjectIdentity = ObjectIdentity
anxsyncports = _Anxsyncports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 9)
)
_AnxTrapHostInfo_ObjectIdentity = ObjectIdentity
anxTrapHostInfo = _AnxTrapHostInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 10)
)
_Anxt1_ObjectIdentity = ObjectIdentity
anxt1 = _Anxt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 11)
)
_Anxpri_ObjectIdentity = ObjectIdentity
anxpri = _Anxpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 12)
)
_Anxinterface_ObjectIdentity = ObjectIdentity
anxinterface = _Anxinterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 13)
)
_Anxtunnelport_ObjectIdentity = ObjectIdentity
anxtunnelport = _Anxtunnelport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 14)
)
_Anxgrestats_ObjectIdentity = ObjectIdentity
anxgrestats = _Anxgrestats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 15)
)
_Callmgmt_ObjectIdentity = ObjectIdentity
callmgmt = _Callmgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 16)
)
_AnxModem_ObjectIdentity = ObjectIdentity
anxModem = _AnxModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 100)
)
_Anxchascommon_ObjectIdentity = ObjectIdentity
anxchascommon = _Anxchascommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 101)
)
_Anxchas_ObjectIdentity = ObjectIdentity
anxchas = _Anxchas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 102)
)
_RadiusClient_ObjectIdentity = ObjectIdentity
radiusClient = _RadiusClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 103)
)
_RadiusConfig_ObjectIdentity = ObjectIdentity
radiusConfig = _RadiusConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 103, 1)
)
_RadiusStats_ObjectIdentity = ObjectIdentity
radiusStats = _RadiusStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 103, 2)
)
_Anxgsystats_ObjectIdentity = ObjectIdentity
anxgsystats = _Anxgsystats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 104)
)
_Anxccpstats_ObjectIdentity = ObjectIdentity
anxccpstats = _Anxccpstats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 105)
)
_Anxexperimental_ObjectIdentity = ObjectIdentity
anxexperimental = _Anxexperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 3)
)
_RacTraps_ObjectIdentity = ObjectIdentity
racTraps = _RacTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 100)
)
_RacTrapObjects_ObjectIdentity = ObjectIdentity
racTrapObjects = _RacTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 100, 1)
)
_WanTrapObj_ObjectIdentity = ObjectIdentity
wanTrapObj = _WanTrapObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 1)
)
_ModemTrapObj_ObjectIdentity = ObjectIdentity
modemTrapObj = _ModemTrapObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 2)
)
_CallmgmtTrapObj_ObjectIdentity = ObjectIdentity
callmgmtTrapObj = _CallmgmtTrapObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 3)
)
_GenericTrapObj_ObjectIdentity = ObjectIdentity
genericTrapObj = _GenericTrapObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 100, 1, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLO-MIB-SMI",
    **{"xylogics": xylogics,
       "prod": prod,
       "prodannex": prodannex,
       "mibversion": mibversion,
       "prodoid": prodoid,
       "unknown": unknown,
       "annexII": annexII,
       "annex3": annex3,
       "microanx": microanx,
       "microels": microels,
       "csmim1": csmim1,
       "ods": ods,
       "bay5390": bay5390,
       "csmim2": csmim2,
       "annex2000": annex2000,
       "microcs": microcs,
       "annex4000": annex4000,
       "a3Com": a3Com,
       "csmim-t1": csmim_t1,
       "ra6100": ra6100,
       "ra6300": ra6300,
       "bay5391": bay5391,
       "bay5393": bay5393,
       "bay5399": bay5399,
       "annex": annex,
       "hw": hw,
       "sw": sw,
       "ports": ports,
       "parallelport": parallelport,
       "annexconfig": annexconfig,
       "anxigmpconfig": anxigmpconfig,
       "annexcmds": annexcmds,
       "annexlatstats": annexlatstats,
       "interfacerip": interfacerip,
       "anxsyncports": anxsyncports,
       "anxTrapHostInfo": anxTrapHostInfo,
       "anxt1": anxt1,
       "anxpri": anxpri,
       "anxinterface": anxinterface,
       "anxtunnelport": anxtunnelport,
       "anxgrestats": anxgrestats,
       "callmgmt": callmgmt,
       "anxModem": anxModem,
       "anxchascommon": anxchascommon,
       "anxchas": anxchas,
       "radiusClient": radiusClient,
       "radiusConfig": radiusConfig,
       "radiusStats": radiusStats,
       "anxgsystats": anxgsystats,
       "anxccpstats": anxccpstats,
       "anxexperimental": anxexperimental,
       "racTraps": racTraps,
       "racTrapObjects": racTrapObjects,
       "wanTrapObj": wanTrapObj,
       "modemTrapObj": modemTrapObj,
       "callmgmtTrapObj": callmgmtTrapObj,
       "genericTrapObj": genericTrapObj}
)
