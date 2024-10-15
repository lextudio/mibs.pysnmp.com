# SNMP MIB module (ENTERASYS-AAA-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-AAA-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:41 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

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

etsysAAAPolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 51)
)
etsysAAAPolicyMIB.setRevisions(
        ("2004-07-29 19:06",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AAAProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("none", 2),
          ("radius", 3),
          ("tacacs", 4))
    )



# MIB Managed Objects in the order of their OIDs

_EtsysAAAPolicyObjects_ObjectIdentity = ObjectIdentity
etsysAAAPolicyObjects = _EtsysAAAPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1)
)
_EtsysAAAPolicyMgmtAccess_ObjectIdentity = ObjectIdentity
etsysAAAPolicyMgmtAccess = _EtsysAAAPolicyMgmtAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1)
)
_EtsysAAAMgmtAccessTable_Object = MibTable
etsysAAAMgmtAccessTable = _EtsysAAAMgmtAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysAAAMgmtAccessTable.setStatus("current")
_EtsysAAAMgmtAccessEntry_Object = MibTableRow
etsysAAAMgmtAccessEntry = _EtsysAAAMgmtAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1, 1)
)
etsysAAAMgmtAccessEntry.setIndexNames(
    (0, "ENTERASYS-AAA-POLICY-MIB", "etsysAAAMgmtAccessProtocol"),
)
if mibBuilder.loadTexts:
    etsysAAAMgmtAccessEntry.setStatus("current")


class _EtsysAAAMgmtAccessProtocol_Type(Integer32):
    """Custom type etsysAAAMgmtAccessProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("allProtocols", 1)
    )


_EtsysAAAMgmtAccessProtocol_Type.__name__ = "Integer32"
_EtsysAAAMgmtAccessProtocol_Object = MibTableColumn
etsysAAAMgmtAccessProtocol = _EtsysAAAMgmtAccessProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1, 1, 1),
    _EtsysAAAMgmtAccessProtocol_Type()
)
etsysAAAMgmtAccessProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysAAAMgmtAccessProtocol.setStatus("current")


class _EtsysAAAMgmtRemoteAuthProtocol_Type(AAAProtocol):
    """Custom type etsysAAAMgmtRemoteAuthProtocol based on AAAProtocol"""


_EtsysAAAMgmtRemoteAuthProtocol_Object = MibTableColumn
etsysAAAMgmtRemoteAuthProtocol = _EtsysAAAMgmtRemoteAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1, 1, 2),
    _EtsysAAAMgmtRemoteAuthProtocol_Type()
)
etsysAAAMgmtRemoteAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAAAMgmtRemoteAuthProtocol.setStatus("current")


class _EtsysAAAMgmtRemoteAcctProtocol_Type(AAAProtocol):
    """Custom type etsysAAAMgmtRemoteAcctProtocol based on AAAProtocol"""


_EtsysAAAMgmtRemoteAcctProtocol_Object = MibTableColumn
etsysAAAMgmtRemoteAcctProtocol = _EtsysAAAMgmtRemoteAcctProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1, 1, 3),
    _EtsysAAAMgmtRemoteAcctProtocol_Type()
)
etsysAAAMgmtRemoteAcctProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAAAMgmtRemoteAcctProtocol.setStatus("current")
_EtsysAAAPolicyMIBConformance_ObjectIdentity = ObjectIdentity
etsysAAAPolicyMIBConformance = _EtsysAAAPolicyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2)
)
_EtsysAAAPolicyMIBCompliances_ObjectIdentity = ObjectIdentity
etsysAAAPolicyMIBCompliances = _EtsysAAAPolicyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2, 1)
)
_EtsysAAAPolicyMIBGroups_ObjectIdentity = ObjectIdentity
etsysAAAPolicyMIBGroups = _EtsysAAAPolicyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2, 2)
)

# Managed Objects groups

etsysAAAPolicyMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2, 2, 1)
)
etsysAAAPolicyMgmtGroup.setObjects(
      *(("ENTERASYS-AAA-POLICY-MIB", "etsysAAAMgmtRemoteAuthProtocol"),
        ("ENTERASYS-AAA-POLICY-MIB", "etsysAAAMgmtRemoteAcctProtocol"))
)
if mibBuilder.loadTexts:
    etsysAAAPolicyMgmtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysAAAPolicyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysAAAPolicyMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-AAA-POLICY-MIB",
    **{"AAAProtocol": AAAProtocol,
       "etsysAAAPolicyMIB": etsysAAAPolicyMIB,
       "etsysAAAPolicyObjects": etsysAAAPolicyObjects,
       "etsysAAAPolicyMgmtAccess": etsysAAAPolicyMgmtAccess,
       "etsysAAAMgmtAccessTable": etsysAAAMgmtAccessTable,
       "etsysAAAMgmtAccessEntry": etsysAAAMgmtAccessEntry,
       "etsysAAAMgmtAccessProtocol": etsysAAAMgmtAccessProtocol,
       "etsysAAAMgmtRemoteAuthProtocol": etsysAAAMgmtRemoteAuthProtocol,
       "etsysAAAMgmtRemoteAcctProtocol": etsysAAAMgmtRemoteAcctProtocol,
       "etsysAAAPolicyMIBConformance": etsysAAAPolicyMIBConformance,
       "etsysAAAPolicyMIBCompliances": etsysAAAPolicyMIBCompliances,
       "etsysAAAPolicyMIBCompliance": etsysAAAPolicyMIBCompliance,
       "etsysAAAPolicyMIBGroups": etsysAAAPolicyMIBGroups,
       "etsysAAAPolicyMgmtGroup": etsysAAAPolicyMgmtGroup}
)
