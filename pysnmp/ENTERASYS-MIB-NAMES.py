# SNMP MIB module (ENTERASYS-MIB-NAMES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-MIB-NAMES
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:39 2024
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

etsysModuleName = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 1)
)
etsysModuleName.setRevisions(
        ("2003-11-06 15:15",
         "2003-10-23 17:19",
         "2002-06-14 16:02",
         "2002-06-14 14:02",
         "2000-11-13 21:21",
         "2000-10-05 13:00",
         "2000-04-07 00:00",
         "2000-03-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Enterasys_ObjectIdentity = ObjectIdentity
enterasys = _Enterasys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624)
)
if mibBuilder.loadTexts:
    enterasys.setStatus("current")
_EtsysMibs_ObjectIdentity = ObjectIdentity
etsysMibs = _EtsysMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1)
)
_EtsysNamesMib_ObjectIdentity = ObjectIdentity
etsysNamesMib = _EtsysNamesMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 1)
)
if mibBuilder.loadTexts:
    etsysNamesMib.setStatus("obsolete")
_EtsysModules_ObjectIdentity = ObjectIdentity
etsysModules = _EtsysModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2)
)
_EtsysConformance_ObjectIdentity = ObjectIdentity
etsysConformance = _EtsysConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 3)
)
if mibBuilder.loadTexts:
    etsysConformance.setStatus("obsolete")
_EtsysConformName_ObjectIdentity = ObjectIdentity
etsysConformName = _EtsysConformName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysConformName.setStatus("obsolete")
_EtsysConformOID_ObjectIdentity = ObjectIdentity
etsysConformOID = _EtsysConformOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 3, 2)
)
if mibBuilder.loadTexts:
    etsysConformOID.setStatus("obsolete")
_EtsysOids_ObjectIdentity = ObjectIdentity
etsysOids = _EtsysOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2)
)
_EtsysAgentCaps_ObjectIdentity = ObjectIdentity
etsysAgentCaps = _EtsysAgentCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 3)
)
_EtsysX509Pki_ObjectIdentity = ObjectIdentity
etsysX509Pki = _EtsysX509Pki_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 509)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-MIB-NAMES",
    **{"enterasys": enterasys,
       "etsysMibs": etsysMibs,
       "etsysNamesMib": etsysNamesMib,
       "etsysModules": etsysModules,
       "etsysModuleName": etsysModuleName,
       "etsysConformance": etsysConformance,
       "etsysConformName": etsysConformName,
       "etsysConformOID": etsysConformOID,
       "etsysOids": etsysOids,
       "etsysAgentCaps": etsysAgentCaps,
       "etsysX509Pki": etsysX509Pki}
)
