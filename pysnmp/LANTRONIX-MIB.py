# SNMP MIB module (LANTRONIX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LANTRONIX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:20 2024
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

lantronix = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 244)
)
lantronix.setRevisions(
        ("2007-03-01 00:00",
         "2006-11-10 00:00",
         "2004-12-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1)
)
_Slc_ObjectIdentity = ObjectIdentity
slc = _Slc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1)
)
_Slk_ObjectIdentity = ObjectIdentity
slk = _Slk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 8)
)
_Slp_ObjectIdentity = ObjectIdentity
slp = _Slp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 9)
)
_Slm_ObjectIdentity = ObjectIdentity
slm = _Slm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 10)
)
_Sls_ObjectIdentity = ObjectIdentity
sls = _Sls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 11)
)
_Slb_ObjectIdentity = ObjectIdentity
slb = _Slb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 12)
)
_Evo_ObjectIdentity = ObjectIdentity
evo = _Evo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 13)
)
_Ltxlna_ObjectIdentity = ObjectIdentity
ltxlna = _Ltxlna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 10)
)
_Ltxlrp_ObjectIdentity = ObjectIdentity
ltxlrp = _Ltxlrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 11)
)
_Ltxlsw_ObjectIdentity = ObjectIdentity
ltxlsw = _Ltxlsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANTRONIX-MIB",
    **{"lantronix": lantronix,
       "products": products,
       "slc": slc,
       "slk": slk,
       "slp": slp,
       "slm": slm,
       "sls": sls,
       "slb": slb,
       "evo": evo,
       "ltxlna": ltxlna,
       "ltxlrp": ltxlrp,
       "ltxlsw": ltxlsw}
)
