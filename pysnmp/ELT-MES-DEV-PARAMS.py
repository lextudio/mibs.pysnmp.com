# SNMP MIB module (ELT-MES-DEV-PARAMS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELT-MES-DEV-PARAMS
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:57 2024
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(rndImageInfoEntry,) = mibBuilder.importSymbols(
    "RADLAN-DEVICEPARAMS-MIB",
    "rndImageInfoEntry")

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

eltMesDevParams = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 2)
)
eltMesDevParams.setRevisions(
        ("2015-09-16 00:00",
         "2012-12-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesBootPassword_ObjectIdentity = ObjectIdentity
eltMesBootPassword = _EltMesBootPassword_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 2, 17)
)
_EltImageInfoTable_Object = MibTable
eltImageInfoTable = _EltImageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 2, 18)
)
if mibBuilder.loadTexts:
    eltImageInfoTable.setStatus("current")
_EltImageInfoEntry_Object = MibTableRow
eltImageInfoEntry = _EltImageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 2, 18, 1)
)
if mibBuilder.loadTexts:
    eltImageInfoEntry.setStatus("current")
_EltImage1CommitHash_Type = DisplayString
_EltImage1CommitHash_Object = MibTableColumn
eltImage1CommitHash = _EltImage1CommitHash_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 2, 18, 1, 1),
    _EltImage1CommitHash_Type()
)
eltImage1CommitHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltImage1CommitHash.setStatus("current")
_EltImage2CommitHash_Type = DisplayString
_EltImage2CommitHash_Object = MibTableColumn
eltImage2CommitHash = _EltImage2CommitHash_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 2, 18, 1, 2),
    _EltImage2CommitHash_Type()
)
eltImage2CommitHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltImage2CommitHash.setStatus("current")
rndImageInfoEntry.registerAugmentions(
    ("ELT-MES-DEV-PARAMS",
     "eltImageInfoEntry")
)
eltImageInfoEntry.setIndexNames(*rndImageInfoEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELT-MES-DEV-PARAMS",
    **{"eltMesDevParams": eltMesDevParams,
       "eltMesBootPassword": eltMesBootPassword,
       "eltImageInfoTable": eltImageInfoTable,
       "eltImageInfoEntry": eltImageInfoEntry,
       "eltImage1CommitHash": eltImage1CommitHash,
       "eltImage2CommitHash": eltImage2CommitHash}
)
