# SNMP MIB module (ENTERASYS-JUMBO-ETHERNET-FRAME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-JUMBO-ETHERNET-FRAME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:01 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

etsysJumboEthernetFrameMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 34)
)
etsysJumboEthernetFrameMIB.setRevisions(
        ("2003-01-24 21:26",
         "2002-12-20 21:56")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysJumboEthernetFrame_ObjectIdentity = ObjectIdentity
etsysJumboEthernetFrame = _EtsysJumboEthernetFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1)
)
_EtsysJumboEnetFrameControl_ObjectIdentity = ObjectIdentity
etsysJumboEnetFrameControl = _EtsysJumboEnetFrameControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1)
)
_EtsysJumboEnetFrameTable_Object = MibTable
etsysJumboEnetFrameTable = _EtsysJumboEnetFrameTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysJumboEnetFrameTable.setStatus("current")
_EtsysJumboEnetFrameEntry_Object = MibTableRow
etsysJumboEnetFrameEntry = _EtsysJumboEnetFrameEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1)
)
etsysJumboEnetFrameEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysJumboEnetFrameEntry.setStatus("current")


class _EtsysJumboEnetFrameEnable_Type(EnabledStatus):
    """Custom type etsysJumboEnetFrameEnable based on EnabledStatus"""


_EtsysJumboEnetFrameEnable_Object = MibTableColumn
etsysJumboEnetFrameEnable = _EtsysJumboEnetFrameEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1, 1),
    _EtsysJumboEnetFrameEnable_Type()
)
etsysJumboEnetFrameEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysJumboEnetFrameEnable.setStatus("obsolete")
_EtsysJumboEnetFrameMtu_Type = Integer32
_EtsysJumboEnetFrameMtu_Object = MibTableColumn
etsysJumboEnetFrameMtu = _EtsysJumboEnetFrameMtu_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1, 2),
    _EtsysJumboEnetFrameMtu_Type()
)
etsysJumboEnetFrameMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysJumboEnetFrameMtu.setStatus("current")


class _EtsysJumboEnetFrameAdminStatus_Type(EnabledStatus):
    """Custom type etsysJumboEnetFrameAdminStatus based on EnabledStatus"""


_EtsysJumboEnetFrameAdminStatus_Object = MibTableColumn
etsysJumboEnetFrameAdminStatus = _EtsysJumboEnetFrameAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1, 3),
    _EtsysJumboEnetFrameAdminStatus_Type()
)
etsysJumboEnetFrameAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysJumboEnetFrameAdminStatus.setStatus("current")
_EtsysJumboEnetFrameOperStatus_Type = EnabledStatus
_EtsysJumboEnetFrameOperStatus_Object = MibTableColumn
etsysJumboEnetFrameOperStatus = _EtsysJumboEnetFrameOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1, 4),
    _EtsysJumboEnetFrameOperStatus_Type()
)
etsysJumboEnetFrameOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysJumboEnetFrameOperStatus.setStatus("current")
_EtsysJumboEnetFrameConformance_ObjectIdentity = ObjectIdentity
etsysJumboEnetFrameConformance = _EtsysJumboEnetFrameConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2)
)
_EtsysJumboEnetFrameGroups_ObjectIdentity = ObjectIdentity
etsysJumboEnetFrameGroups = _EtsysJumboEnetFrameGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 1)
)
_EtsysJumboEnetFrameCompliances_ObjectIdentity = ObjectIdentity
etsysJumboEnetFrameCompliances = _EtsysJumboEnetFrameCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 2)
)

# Managed Objects groups

etsysJumboEnetFrameControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 1, 1)
)
etsysJumboEnetFrameControlGroup.setObjects(
      *(("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameEnable"),
        ("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameMtu"))
)
if mibBuilder.loadTexts:
    etsysJumboEnetFrameControlGroup.setStatus("obsolete")

etsysJumboEnetFrameControlGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 1, 2)
)
etsysJumboEnetFrameControlGroup2.setObjects(
      *(("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameMtu"),
        ("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameAdminStatus"),
        ("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameOperStatus"))
)
if mibBuilder.loadTexts:
    etsysJumboEnetFrameControlGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysJumboEnetFrameCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysJumboEnetFrameCompliance.setStatus(
        "obsolete"
    )

etsysJumboEnetFrameCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 2, 2)
)
if mibBuilder.loadTexts:
    etsysJumboEnetFrameCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-JUMBO-ETHERNET-FRAME-MIB",
    **{"etsysJumboEthernetFrameMIB": etsysJumboEthernetFrameMIB,
       "etsysJumboEthernetFrame": etsysJumboEthernetFrame,
       "etsysJumboEnetFrameControl": etsysJumboEnetFrameControl,
       "etsysJumboEnetFrameTable": etsysJumboEnetFrameTable,
       "etsysJumboEnetFrameEntry": etsysJumboEnetFrameEntry,
       "etsysJumboEnetFrameEnable": etsysJumboEnetFrameEnable,
       "etsysJumboEnetFrameMtu": etsysJumboEnetFrameMtu,
       "etsysJumboEnetFrameAdminStatus": etsysJumboEnetFrameAdminStatus,
       "etsysJumboEnetFrameOperStatus": etsysJumboEnetFrameOperStatus,
       "etsysJumboEnetFrameConformance": etsysJumboEnetFrameConformance,
       "etsysJumboEnetFrameGroups": etsysJumboEnetFrameGroups,
       "etsysJumboEnetFrameControlGroup": etsysJumboEnetFrameControlGroup,
       "etsysJumboEnetFrameControlGroup2": etsysJumboEnetFrameControlGroup2,
       "etsysJumboEnetFrameCompliances": etsysJumboEnetFrameCompliances,
       "etsysJumboEnetFrameCompliance": etsysJumboEnetFrameCompliance,
       "etsysJumboEnetFrameCompliance2": etsysJumboEnetFrameCompliance2}
)
