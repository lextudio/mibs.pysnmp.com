# SNMP MIB module (CISCO-L2L3-INTERFACE-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-L2L3-INTERFACE-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:48 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ciscoL2L3IfConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 151)
)
ciscoL2L3IfConfigMIB.setRevisions(
        ("2000-05-10 19:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CL2L3InterfaceMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("routed", 1),
          ("switchport", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoL2L3IfConfigMIBObjects_ObjectIdentity = ObjectIdentity
ciscoL2L3IfConfigMIBObjects = _CiscoL2L3IfConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 1)
)
_CL2L3IfConfig_ObjectIdentity = ObjectIdentity
cL2L3IfConfig = _CL2L3IfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1)
)
_CL2L3IfTable_Object = MibTable
cL2L3IfTable = _CL2L3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cL2L3IfTable.setStatus("current")
_CL2L3IfEntry_Object = MibTableRow
cL2L3IfEntry = _CL2L3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1)
)
cL2L3IfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cL2L3IfEntry.setStatus("current")
_CL2L3IfModeAdmin_Type = CL2L3InterfaceMode
_CL2L3IfModeAdmin_Object = MibTableColumn
cL2L3IfModeAdmin = _CL2L3IfModeAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1, 1),
    _CL2L3IfModeAdmin_Type()
)
cL2L3IfModeAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cL2L3IfModeAdmin.setStatus("current")
_CL2L3IfModeOper_Type = CL2L3InterfaceMode
_CL2L3IfModeOper_Object = MibTableColumn
cL2L3IfModeOper = _CL2L3IfModeOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1, 2),
    _CL2L3IfModeOper_Type()
)
cL2L3IfModeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cL2L3IfModeOper.setStatus("current")
_CiscoL2L3IfConfigMIBConformance_ObjectIdentity = ObjectIdentity
ciscoL2L3IfConfigMIBConformance = _CiscoL2L3IfConfigMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 3)
)
_CiscoL2L3IfConfigMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoL2L3IfConfigMIBCompliances = _CiscoL2L3IfConfigMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 1)
)
_CiscoL2L3IfConfigMIBGroups_ObjectIdentity = ObjectIdentity
ciscoL2L3IfConfigMIBGroups = _CiscoL2L3IfConfigMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 2)
)

# Managed Objects groups

ciscoL2L3IfConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 2, 1)
)
ciscoL2L3IfConfigMIBGroup.setObjects(
      *(("CISCO-L2L3-INTERFACE-CONFIG-MIB", "cL2L3IfModeAdmin"),
        ("CISCO-L2L3-INTERFACE-CONFIG-MIB", "cL2L3IfModeOper"))
)
if mibBuilder.loadTexts:
    ciscoL2L3IfConfigMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoL2L3IfConfigMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoL2L3IfConfigMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-L2L3-INTERFACE-CONFIG-MIB",
    **{"CL2L3InterfaceMode": CL2L3InterfaceMode,
       "ciscoL2L3IfConfigMIB": ciscoL2L3IfConfigMIB,
       "ciscoL2L3IfConfigMIBObjects": ciscoL2L3IfConfigMIBObjects,
       "cL2L3IfConfig": cL2L3IfConfig,
       "cL2L3IfTable": cL2L3IfTable,
       "cL2L3IfEntry": cL2L3IfEntry,
       "cL2L3IfModeAdmin": cL2L3IfModeAdmin,
       "cL2L3IfModeOper": cL2L3IfModeOper,
       "ciscoL2L3IfConfigMIBConformance": ciscoL2L3IfConfigMIBConformance,
       "ciscoL2L3IfConfigMIBCompliances": ciscoL2L3IfConfigMIBCompliances,
       "ciscoL2L3IfConfigMIBCompliance": ciscoL2L3IfConfigMIBCompliance,
       "ciscoL2L3IfConfigMIBGroups": ciscoL2L3IfConfigMIBGroups,
       "ciscoL2L3IfConfigMIBGroup": ciscoL2L3IfConfigMIBGroup}
)
