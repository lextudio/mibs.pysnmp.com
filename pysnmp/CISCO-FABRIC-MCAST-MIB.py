# SNMP MIB module (CISCO-FABRIC-MCAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FABRIC-MCAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:07 2024
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

(entLogicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLogicalIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ciscoFabricMcastMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 255)
)
ciscoFabricMcastMIB.setRevisions(
        ("2002-08-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CfmPoolIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoFabricMcastMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoFabricMcastMIBNotifs = _CiscoFabricMcastMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 0)
)
_CiscoFabricMcastMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFabricMcastMIBObjects = _CiscoFabricMcastMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1)
)
_CfmGeneral_ObjectIdentity = ObjectIdentity
cfmGeneral = _CfmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 1)
)
_CfmGenInfoTotalFgids_Type = Gauge32
_CfmGenInfoTotalFgids_Object = MibScalar
cfmGenInfoTotalFgids = _CfmGenInfoTotalFgids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 1, 1),
    _CfmGenInfoTotalFgids_Type()
)
cfmGenInfoTotalFgids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmGenInfoTotalFgids.setStatus("current")
if mibBuilder.loadTexts:
    cfmGenInfoTotalFgids.setUnits("fgid")
_CfmGenInfoInuseFgids_Type = Gauge32
_CfmGenInfoInuseFgids_Object = MibScalar
cfmGenInfoInuseFgids = _CfmGenInfoInuseFgids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 1, 2),
    _CfmGenInfoInuseFgids_Type()
)
cfmGenInfoInuseFgids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmGenInfoInuseFgids.setStatus("current")
if mibBuilder.loadTexts:
    cfmGenInfoInuseFgids.setUnits("fgid")
_CfmGenInfoHighWaterInuseFgids_Type = Gauge32
_CfmGenInfoHighWaterInuseFgids_Object = MibScalar
cfmGenInfoHighWaterInuseFgids = _CfmGenInfoHighWaterInuseFgids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 1, 3),
    _CfmGenInfoHighWaterInuseFgids_Type()
)
cfmGenInfoHighWaterInuseFgids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmGenInfoHighWaterInuseFgids.setStatus("current")
if mibBuilder.loadTexts:
    cfmGenInfoHighWaterInuseFgids.setUnits("fgid")
_CfmPool_ObjectIdentity = ObjectIdentity
cfmPool = _CfmPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2)
)
_CfmPoolTable_Object = MibTable
cfmPoolTable = _CfmPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfmPoolTable.setStatus("current")
_CfmPoolEntry_Object = MibTableRow
cfmPoolEntry = _CfmPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1)
)
cfmPoolEntry.setIndexNames(
    (0, "CISCO-FABRIC-MCAST-MIB", "cfmPoolId"),
)
if mibBuilder.loadTexts:
    cfmPoolEntry.setStatus("current")
_CfmPoolId_Type = CfmPoolIndex
_CfmPoolId_Object = MibTableColumn
cfmPoolId = _CfmPoolId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 1),
    _CfmPoolId_Type()
)
cfmPoolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmPoolId.setStatus("current")
_CfmPoolName_Type = SnmpAdminString
_CfmPoolName_Object = MibTableColumn
cfmPoolName = _CfmPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 2),
    _CfmPoolName_Type()
)
cfmPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmPoolName.setStatus("current")


class _CfmPoolType_Type(Integer32):
    """Custom type cfmPoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 2),
          ("shared", 1))
    )


_CfmPoolType_Type.__name__ = "Integer32"
_CfmPoolType_Object = MibTableColumn
cfmPoolType = _CfmPoolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 3),
    _CfmPoolType_Type()
)
cfmPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmPoolType.setStatus("current")
_CfmPoolTotalFgids_Type = Gauge32
_CfmPoolTotalFgids_Object = MibTableColumn
cfmPoolTotalFgids = _CfmPoolTotalFgids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 4),
    _CfmPoolTotalFgids_Type()
)
cfmPoolTotalFgids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmPoolTotalFgids.setStatus("current")
if mibBuilder.loadTexts:
    cfmPoolTotalFgids.setUnits("fgid")
_CfmPoolInuseFgids_Type = Gauge32
_CfmPoolInuseFgids_Object = MibTableColumn
cfmPoolInuseFgids = _CfmPoolInuseFgids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 5),
    _CfmPoolInuseFgids_Type()
)
cfmPoolInuseFgids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmPoolInuseFgids.setStatus("current")
if mibBuilder.loadTexts:
    cfmPoolInuseFgids.setUnits("fgid")
_CfmPoolHighWaterInuseFgids_Type = Gauge32
_CfmPoolHighWaterInuseFgids_Object = MibTableColumn
cfmPoolHighWaterInuseFgids = _CfmPoolHighWaterInuseFgids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 6),
    _CfmPoolHighWaterInuseFgids_Type()
)
cfmPoolHighWaterInuseFgids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmPoolHighWaterInuseFgids.setStatus("current")
if mibBuilder.loadTexts:
    cfmPoolHighWaterInuseFgids.setUnits("fgid")
_CfmLr_ObjectIdentity = ObjectIdentity
cfmLr = _CfmLr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 3)
)
_CfmLrTable_Object = MibTable
cfmLrTable = _CfmLrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cfmLrTable.setStatus("current")
_CfmLrEntry_Object = MibTableRow
cfmLrEntry = _CfmLrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 3, 1, 1)
)
cfmLrEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLogicalIndex"),
)
if mibBuilder.loadTexts:
    cfmLrEntry.setStatus("current")
_CfmLrInuseFgids_Type = Gauge32
_CfmLrInuseFgids_Object = MibTableColumn
cfmLrInuseFgids = _CfmLrInuseFgids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 3, 1, 1, 1),
    _CfmLrInuseFgids_Type()
)
cfmLrInuseFgids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmLrInuseFgids.setStatus("current")
if mibBuilder.loadTexts:
    cfmLrInuseFgids.setUnits("fgid")
_CfmLrHighWaterInuseFgids_Type = Gauge32
_CfmLrHighWaterInuseFgids_Object = MibTableColumn
cfmLrHighWaterInuseFgids = _CfmLrHighWaterInuseFgids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 3, 1, 1, 2),
    _CfmLrHighWaterInuseFgids_Type()
)
cfmLrHighWaterInuseFgids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmLrHighWaterInuseFgids.setStatus("current")
if mibBuilder.loadTexts:
    cfmLrHighWaterInuseFgids.setUnits("fgid")
_CiscoFabricMcastMIBConform_ObjectIdentity = ObjectIdentity
ciscoFabricMcastMIBConform = _CiscoFabricMcastMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 2)
)
_CfmMIBCompliances_ObjectIdentity = ObjectIdentity
cfmMIBCompliances = _CfmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 1)
)
_CfmMIBGroups_ObjectIdentity = ObjectIdentity
cfmMIBGroups = _CfmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 2)
)

# Managed Objects groups

cfmGenInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 2, 1)
)
cfmGenInfoGroup.setObjects(
      *(("CISCO-FABRIC-MCAST-MIB", "cfmGenInfoTotalFgids"),
        ("CISCO-FABRIC-MCAST-MIB", "cfmGenInfoInuseFgids"),
        ("CISCO-FABRIC-MCAST-MIB", "cfmGenInfoHighWaterInuseFgids"))
)
if mibBuilder.loadTexts:
    cfmGenInfoGroup.setStatus("current")

cfmPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 2, 2)
)
cfmPoolGroup.setObjects(
      *(("CISCO-FABRIC-MCAST-MIB", "cfmPoolName"),
        ("CISCO-FABRIC-MCAST-MIB", "cfmPoolType"),
        ("CISCO-FABRIC-MCAST-MIB", "cfmPoolTotalFgids"),
        ("CISCO-FABRIC-MCAST-MIB", "cfmPoolInuseFgids"),
        ("CISCO-FABRIC-MCAST-MIB", "cfmPoolHighWaterInuseFgids"))
)
if mibBuilder.loadTexts:
    cfmPoolGroup.setStatus("current")

cfmLrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 2, 3)
)
cfmLrGroup.setObjects(
      *(("CISCO-FABRIC-MCAST-MIB", "cfmLrInuseFgids"),
        ("CISCO-FABRIC-MCAST-MIB", "cfmLrHighWaterInuseFgids"))
)
if mibBuilder.loadTexts:
    cfmLrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cfmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cfmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FABRIC-MCAST-MIB",
    **{"CfmPoolIndex": CfmPoolIndex,
       "ciscoFabricMcastMIB": ciscoFabricMcastMIB,
       "ciscoFabricMcastMIBNotifs": ciscoFabricMcastMIBNotifs,
       "ciscoFabricMcastMIBObjects": ciscoFabricMcastMIBObjects,
       "cfmGeneral": cfmGeneral,
       "cfmGenInfoTotalFgids": cfmGenInfoTotalFgids,
       "cfmGenInfoInuseFgids": cfmGenInfoInuseFgids,
       "cfmGenInfoHighWaterInuseFgids": cfmGenInfoHighWaterInuseFgids,
       "cfmPool": cfmPool,
       "cfmPoolTable": cfmPoolTable,
       "cfmPoolEntry": cfmPoolEntry,
       "cfmPoolId": cfmPoolId,
       "cfmPoolName": cfmPoolName,
       "cfmPoolType": cfmPoolType,
       "cfmPoolTotalFgids": cfmPoolTotalFgids,
       "cfmPoolInuseFgids": cfmPoolInuseFgids,
       "cfmPoolHighWaterInuseFgids": cfmPoolHighWaterInuseFgids,
       "cfmLr": cfmLr,
       "cfmLrTable": cfmLrTable,
       "cfmLrEntry": cfmLrEntry,
       "cfmLrInuseFgids": cfmLrInuseFgids,
       "cfmLrHighWaterInuseFgids": cfmLrHighWaterInuseFgids,
       "ciscoFabricMcastMIBConform": ciscoFabricMcastMIBConform,
       "cfmMIBCompliances": cfmMIBCompliances,
       "cfmMIBCompliance": cfmMIBCompliance,
       "cfmMIBGroups": cfmMIBGroups,
       "cfmGenInfoGroup": cfmGenInfoGroup,
       "cfmPoolGroup": cfmPoolGroup,
       "cfmLrGroup": cfmLrGroup}
)
