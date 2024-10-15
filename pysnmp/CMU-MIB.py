# SNMP MIB module (CMU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CMU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:53 2024
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

_Proteon_ObjectIdentity = ObjectIdentity
proteon = _Proteon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1)
)
_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_Cmu_ObjectIdentity = ObjectIdentity
cmu = _Cmu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3)
)
_Unix_ObjectIdentity = ObjectIdentity
unix = _Unix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4)
)
_Acc_ObjectIdentity = ObjectIdentity
acc = _Acc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5)
)
_Twg_ObjectIdentity = ObjectIdentity
twg = _Twg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6)
)
_Cayman_ObjectIdentity = ObjectIdentity
cayman = _Cayman_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7)
)
_Psi_ObjectIdentity = ObjectIdentity
psi = _Psi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8)
)
_Cisco_ObjectIdentity = ObjectIdentity
cisco = _Cisco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9)
)
_Nsc_ObjectIdentity = ObjectIdentity
nsc = _Nsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10)
)
_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Epilogue_ObjectIdentity = ObjectIdentity
epilogue = _Epilogue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12)
)
_Utk_ObjectIdentity = ObjectIdentity
utk = _Utk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13)
)
_Bbn_ObjectIdentity = ObjectIdentity
bbn = _Bbn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14)
)
_Xylogics_ObjectIdentity = ObjectIdentity
xylogics = _Xylogics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15)
)
_Timeplex_ObjectIdentity = ObjectIdentity
timeplex = _Timeplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16)
)
_Canstar_ObjectIdentity = ObjectIdentity
canstar = _Canstar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17)
)
_Wellfleet_ObjectIdentity = ObjectIdentity
wellfleet = _Wellfleet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18)
)
_Trw_ObjectIdentity = ObjectIdentity
trw = _Trw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19)
)
_Mit_ObjectIdentity = ObjectIdentity
mit = _Mit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20)
)
_Eon_ObjectIdentity = ObjectIdentity
eon = _Eon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21)
)
_Spartacus_ObjectIdentity = ObjectIdentity
spartacus = _Spartacus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22)
)
_Excelan_ObjectIdentity = ObjectIdentity
excelan = _Excelan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_Spider_ObjectIdentity = ObjectIdentity
spider = _Spider_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24)
)
_Nsfnet_ObjectIdentity = ObjectIdentity
nsfnet = _Nsfnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25)
)
_Hls_ObjectIdentity = ObjectIdentity
hls = _Hls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26)
)
_Xyplex_ObjectIdentity = ObjectIdentity
xyplex = _Xyplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33)
)
_Cray_ObjectIdentity = ObjectIdentity
cray = _Cray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34)
)
_Dec_ObjectIdentity = ObjectIdentity
dec = _Dec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36)
)
_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Synoptics_ObjectIdentity = ObjectIdentity
synoptics = _Synoptics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45)
)
_Tgv_ObjectIdentity = ObjectIdentity
tgv = _Tgv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 58)
)
_Apple_ObjectIdentity = ObjectIdentity
apple = _Apple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 63)
)
_Nat_ObjectIdentity = ObjectIdentity
nat = _Nat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86)
)
_Snmp_research_ObjectIdentity = ObjectIdentity
snmp_research = _Snmp_research_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 99)
)
_Ftp_ObjectIdentity = ObjectIdentity
ftp = _Ftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 121)
)
_Shiva_ObjectIdentity = ObjectIdentity
shiva = _Shiva_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166)
)
_Transarc_ObjectIdentity = ObjectIdentity
transarc = _Transarc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 257)
)
_Lexcel_ObjectIdentity = ObjectIdentity
lexcel = _Lexcel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 379)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CMU-MIB",
    **{"proteon": proteon,
       "ibm": ibm,
       "cmu": cmu,
       "unix": unix,
       "acc": acc,
       "twg": twg,
       "cayman": cayman,
       "psi": psi,
       "cisco": cisco,
       "nsc": nsc,
       "hp": hp,
       "epilogue": epilogue,
       "utk": utk,
       "bbn": bbn,
       "xylogics": xylogics,
       "timeplex": timeplex,
       "canstar": canstar,
       "wellfleet": wellfleet,
       "trw": trw,
       "mit": mit,
       "eon": eon,
       "spartacus": spartacus,
       "excelan": excelan,
       "spider": spider,
       "nsfnet": nsfnet,
       "hls": hls,
       "xyplex": xyplex,
       "cray": cray,
       "dec": dec,
       "sun": sun,
       "synoptics": synoptics,
       "tgv": tgv,
       "apple": apple,
       "nat": nat,
       "snmp-research": snmp_research,
       "ftp": ftp,
       "shiva": shiva,
       "transarc": transarc,
       "lexcel": lexcel}
)
