# SNMP MIB module (CISCO-DS0-CROSS-CONNECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DS0-CROSS-CONNECT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:01 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDs0CrossConnectMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999)
)
ciscoDs0CrossConnectMIB.setRevisions(
        ("2003-03-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDs0CrossConnectMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDs0CrossConnectMIBNotifs = _CiscoDs0CrossConnectMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 0)
)
_CiscoDs0CrossConnectMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDs0CrossConnectMIBObjects = _CiscoDs0CrossConnectMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1)
)
_CDs0CrossConnectConfig_ObjectIdentity = ObjectIdentity
cDs0CrossConnectConfig = _CDs0CrossConnectConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1)
)
_Cds0CrossConnectConfigTable_Object = MibTable
cds0CrossConnectConfigTable = _Cds0CrossConnectConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cds0CrossConnectConfigTable.setStatus("current")
_Cds0CrossConnectConfigEntry_Object = MibTableRow
cds0CrossConnectConfigEntry = _Cds0CrossConnectConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1)
)
cds0CrossConnectConfigEntry.setIndexNames(
    (0, "CISCO-DS0-CROSS-CONNECT-MIB", "cds0Endpt1Ds1"),
    (0, "CISCO-DS0-CROSS-CONNECT-MIB", "cds0Endpt1Ds0Group"),
)
if mibBuilder.loadTexts:
    cds0CrossConnectConfigEntry.setStatus("current")
_Cds0Endpt1Ds1_Type = InterfaceIndex
_Cds0Endpt1Ds1_Object = MibTableColumn
cds0Endpt1Ds1 = _Cds0Endpt1Ds1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1),
    _Cds0Endpt1Ds1_Type()
)
cds0Endpt1Ds1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cds0Endpt1Ds1.setStatus("current")


class _Cds0Endpt1Ds0Group_Type(Unsigned32):
    """Custom type cds0Endpt1Ds0Group based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Cds0Endpt1Ds0Group_Type.__name__ = "Unsigned32"
_Cds0Endpt1Ds0Group_Object = MibTableColumn
cds0Endpt1Ds0Group = _Cds0Endpt1Ds0Group_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 2),
    _Cds0Endpt1Ds0Group_Type()
)
cds0Endpt1Ds0Group.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cds0Endpt1Ds0Group.setStatus("current")
_Cds0Endpt2Ds1_Type = InterfaceIndex
_Cds0Endpt2Ds1_Object = MibTableColumn
cds0Endpt2Ds1 = _Cds0Endpt2Ds1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 3),
    _Cds0Endpt2Ds1_Type()
)
cds0Endpt2Ds1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds0Endpt2Ds1.setStatus("current")


class _Cds0Endpt2Ds0Group_Type(Unsigned32):
    """Custom type cds0Endpt2Ds0Group based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Cds0Endpt2Ds0Group_Type.__name__ = "Unsigned32"
_Cds0Endpt2Ds0Group_Object = MibTableColumn
cds0Endpt2Ds0Group = _Cds0Endpt2Ds0Group_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 4),
    _Cds0Endpt2Ds0Group_Type()
)
cds0Endpt2Ds0Group.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds0Endpt2Ds0Group.setStatus("current")
_Cds0ConnRowStatus_Type = RowStatus
_Cds0ConnRowStatus_Object = MibTableColumn
cds0ConnRowStatus = _Cds0ConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 5),
    _Cds0ConnRowStatus_Type()
)
cds0ConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds0ConnRowStatus.setStatus("current")
_CiscoDs0CrossConnectMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDs0CrossConnectMIBConformance = _CiscoDs0CrossConnectMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2)
)
_CiscoDs0CrossConnectMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDs0CrossConnectMIBCompliances = _CiscoDs0CrossConnectMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1)
)
_CiscoDs0CrossConnectMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDs0CrossConnectMIBGroups = _CiscoDs0CrossConnectMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2)
)

# Managed Objects groups

cDs0CrossConnectConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 1)
)
cDs0CrossConnectConfigGroup.setObjects(
      *(("CISCO-DS0-CROSS-CONNECT-MIB", "cds0Endpt2Ds1"),
        ("CISCO-DS0-CROSS-CONNECT-MIB", "cds0Endpt2Ds0Group"),
        ("CISCO-DS0-CROSS-CONNECT-MIB", "cds0ConnRowStatus"))
)
if mibBuilder.loadTexts:
    cDs0CrossConnectConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDs0CrossConnectMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDs0CrossConnectMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DS0-CROSS-CONNECT-MIB",
    **{"ciscoDs0CrossConnectMIB": ciscoDs0CrossConnectMIB,
       "ciscoDs0CrossConnectMIBNotifs": ciscoDs0CrossConnectMIBNotifs,
       "ciscoDs0CrossConnectMIBObjects": ciscoDs0CrossConnectMIBObjects,
       "cDs0CrossConnectConfig": cDs0CrossConnectConfig,
       "cds0CrossConnectConfigTable": cds0CrossConnectConfigTable,
       "cds0CrossConnectConfigEntry": cds0CrossConnectConfigEntry,
       "cds0Endpt1Ds1": cds0Endpt1Ds1,
       "cds0Endpt1Ds0Group": cds0Endpt1Ds0Group,
       "cds0Endpt2Ds1": cds0Endpt2Ds1,
       "cds0Endpt2Ds0Group": cds0Endpt2Ds0Group,
       "cds0ConnRowStatus": cds0ConnRowStatus,
       "ciscoDs0CrossConnectMIBConformance": ciscoDs0CrossConnectMIBConformance,
       "ciscoDs0CrossConnectMIBCompliances": ciscoDs0CrossConnectMIBCompliances,
       "ciscoDs0CrossConnectMIBCompliance": ciscoDs0CrossConnectMIBCompliance,
       "ciscoDs0CrossConnectMIBGroups": ciscoDs0CrossConnectMIBGroups,
       "cDs0CrossConnectConfigGroup": cDs0CrossConnectConfigGroup}
)
