# SNMP MIB module (NT-Reference-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NT-Reference-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:44 2024
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

_Nt_ObjectIdentity = ObjectIdentity
nt = _Nt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562)
)
_Meridian_ObjectIdentity = ObjectIdentity
meridian = _Meridian_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 0)
)
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 1)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 2)
)
_EntityNaming_ObjectIdentity = ObjectIdentity
entityNaming = _EntityNaming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 2, 0)
)
_NetworkID_ObjectIdentity = ObjectIdentity
networkID = _NetworkID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 2, 0, 0)
)
_CybeleNaming_ObjectIdentity = ObjectIdentity
cybeleNaming = _CybeleNaming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 2, 0, 1)
)
_NgenNaming_ObjectIdentity = ObjectIdentity
ngenNaming = _NgenNaming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 2, 0, 2)
)
_MailNaming_ObjectIdentity = ObjectIdentity
mailNaming = _MailNaming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 2, 0, 3)
)
_MobilityNmaing_ObjectIdentity = ObjectIdentity
mobilityNmaing = _MobilityNmaing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 2, 0, 4)
)
_Smp_ObjectIdentity = ObjectIdentity
smp = _Smp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 3)
)
_Cybele_ObjectIdentity = ObjectIdentity
cybele = _Cybele_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 4)
)
_Mobility_ObjectIdentity = ObjectIdentity
mobility = _Mobility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 5)
)
_CallProcessing_ObjectIdentity = ObjectIdentity
callProcessing = _CallProcessing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 6)
)
_Iccm_ObjectIdentity = ObjectIdentity
iccm = _Iccm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 7)
)
_Ngen_ObjectIdentity = ObjectIdentity
ngen = _Ngen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 8)
)
_Amber_ObjectIdentity = ObjectIdentity
amber = _Amber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 3, 9)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NT-Reference-MIB",
    **{"nt": nt,
       "meridian": meridian,
       "experimental": experimental,
       "modules": modules,
       "common": common,
       "entityNaming": entityNaming,
       "networkID": networkID,
       "cybeleNaming": cybeleNaming,
       "ngenNaming": ngenNaming,
       "mailNaming": mailNaming,
       "mobilityNmaing": mobilityNmaing,
       "smp": smp,
       "cybele": cybele,
       "mobility": mobility,
       "callProcessing": callProcessing,
       "iccm": iccm,
       "ngen": ngen,
       "amber": amber}
)
