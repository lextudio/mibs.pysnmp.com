# SNMP MIB module (CISCO-DS0BUNDLE-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DS0BUNDLE-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:02 2024
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

(dsx0BundleEntry,) = mibBuilder.importSymbols(
    "CISCO-DS0BUNDLE-MIB",
    "dsx0BundleEntry")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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

ciscoDs0BundleExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Ds0ChannelList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDs0BundleExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDs0BundleExtMIBObjects = _CiscoDs0BundleExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 1)
)
_Cdsx0BundleConfig_ObjectIdentity = ObjectIdentity
cdsx0BundleConfig = _Cdsx0BundleConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1)
)
_Cdsx0BundleExtTable_Object = MibTable
cdsx0BundleExtTable = _Cdsx0BundleExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdsx0BundleExtTable.setStatus("current")
_Cdsx0BundleExtEntry_Object = MibTableRow
cdsx0BundleExtEntry = _Cdsx0BundleExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdsx0BundleExtEntry.setStatus("current")
_Cdsx0BundleExtDs1Index_Type = InterfaceIndex
_Cdsx0BundleExtDs1Index_Object = MibTableColumn
cdsx0BundleExtDs1Index = _Cdsx0BundleExtDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1, 1, 1),
    _Cdsx0BundleExtDs1Index_Type()
)
cdsx0BundleExtDs1Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsx0BundleExtDs1Index.setStatus("current")
_Cdsx0BundleExtChannelMap_Type = Ds0ChannelList
_Cdsx0BundleExtChannelMap_Object = MibTableColumn
cdsx0BundleExtChannelMap = _Cdsx0BundleExtChannelMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1, 1, 2),
    _Cdsx0BundleExtChannelMap_Type()
)
cdsx0BundleExtChannelMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsx0BundleExtChannelMap.setStatus("current")


class _Cdsx0BundleExtEncapType_Type(Integer32):
    """Custom type cdsx0BundleExtEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atmFuni", 2),
          ("frameRelay", 3),
          ("none", 1))
    )


_Cdsx0BundleExtEncapType_Type.__name__ = "Integer32"
_Cdsx0BundleExtEncapType_Object = MibTableColumn
cdsx0BundleExtEncapType = _Cdsx0BundleExtEncapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1, 1, 3),
    _Cdsx0BundleExtEncapType_Type()
)
cdsx0BundleExtEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsx0BundleExtEncapType.setStatus("current")


class _Cdsx0BundleExtChannelRate_Type(Integer32):
    """Custom type cdsx0BundleExtChannelRate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate56", 1),
          ("rate64", 2))
    )


_Cdsx0BundleExtChannelRate_Type.__name__ = "Integer32"
_Cdsx0BundleExtChannelRate_Object = MibTableColumn
cdsx0BundleExtChannelRate = _Cdsx0BundleExtChannelRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1, 1, 4),
    _Cdsx0BundleExtChannelRate_Type()
)
cdsx0BundleExtChannelRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsx0BundleExtChannelRate.setStatus("current")
_Cdsx0BundleInfo_ObjectIdentity = ObjectIdentity
cdsx0BundleInfo = _Cdsx0BundleInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 2)
)
_Cdsx0BundleUseTable_Object = MibTable
cdsx0BundleUseTable = _Cdsx0BundleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdsx0BundleUseTable.setStatus("current")
_Cdsx0BundleUseEntry_Object = MibTableRow
cdsx0BundleUseEntry = _Cdsx0BundleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 2, 1, 1)
)
cdsx0BundleUseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdsx0BundleUseEntry.setStatus("current")
_Cdsx0BundleUseDs0Used_Type = Ds0ChannelList
_Cdsx0BundleUseDs0Used_Object = MibTableColumn
cdsx0BundleUseDs0Used = _Cdsx0BundleUseDs0Used_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 2, 1, 1, 1),
    _Cdsx0BundleUseDs0Used_Type()
)
cdsx0BundleUseDs0Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsx0BundleUseDs0Used.setStatus("current")
_CiscoDs0BundleExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDs0BundleExtMIBConformance = _CiscoDs0BundleExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 3)
)
_CiscoDs0BundleExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDs0BundleExtMIBCompliances = _CiscoDs0BundleExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 3, 1)
)
_CiscoDs0BundleExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDs0BundleExtMIBGroups = _CiscoDs0BundleExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 3, 2)
)
dsx0BundleEntry.registerAugmentions(
    ("CISCO-DS0BUNDLE-EXT-MIB",
     "cdsx0BundleExtEntry")
)
cdsx0BundleExtEntry.setIndexNames(*dsx0BundleEntry.getIndexNames())

# Managed Objects groups

ciscoDs0BundleExtConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 3, 2, 1)
)
ciscoDs0BundleExtConfigGroup.setObjects(
      *(("CISCO-DS0BUNDLE-EXT-MIB", "cdsx0BundleExtDs1Index"),
        ("CISCO-DS0BUNDLE-EXT-MIB", "cdsx0BundleExtChannelMap"),
        ("CISCO-DS0BUNDLE-EXT-MIB", "cdsx0BundleExtEncapType"),
        ("CISCO-DS0BUNDLE-EXT-MIB", "cdsx0BundleExtChannelRate"))
)
if mibBuilder.loadTexts:
    ciscoDs0BundleExtConfigGroup.setStatus("current")

ciscoDs0BundleExtInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 3, 2, 2)
)
ciscoDs0BundleExtInfoGroup.setObjects(
    ("CISCO-DS0BUNDLE-EXT-MIB", "cdsx0BundleUseDs0Used")
)
if mibBuilder.loadTexts:
    ciscoDs0BundleExtInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDs0BundleExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 33, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDs0BundleExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DS0BUNDLE-EXT-MIB",
    **{"Ds0ChannelList": Ds0ChannelList,
       "ciscoDs0BundleExtMIB": ciscoDs0BundleExtMIB,
       "ciscoDs0BundleExtMIBObjects": ciscoDs0BundleExtMIBObjects,
       "cdsx0BundleConfig": cdsx0BundleConfig,
       "cdsx0BundleExtTable": cdsx0BundleExtTable,
       "cdsx0BundleExtEntry": cdsx0BundleExtEntry,
       "cdsx0BundleExtDs1Index": cdsx0BundleExtDs1Index,
       "cdsx0BundleExtChannelMap": cdsx0BundleExtChannelMap,
       "cdsx0BundleExtEncapType": cdsx0BundleExtEncapType,
       "cdsx0BundleExtChannelRate": cdsx0BundleExtChannelRate,
       "cdsx0BundleInfo": cdsx0BundleInfo,
       "cdsx0BundleUseTable": cdsx0BundleUseTable,
       "cdsx0BundleUseEntry": cdsx0BundleUseEntry,
       "cdsx0BundleUseDs0Used": cdsx0BundleUseDs0Used,
       "ciscoDs0BundleExtMIBConformance": ciscoDs0BundleExtMIBConformance,
       "ciscoDs0BundleExtMIBCompliances": ciscoDs0BundleExtMIBCompliances,
       "ciscoDs0BundleExtMIBCompliance": ciscoDs0BundleExtMIBCompliance,
       "ciscoDs0BundleExtMIBGroups": ciscoDs0BundleExtMIBGroups,
       "ciscoDs0BundleExtConfigGroup": ciscoDs0BundleExtConfigGroup,
       "ciscoDs0BundleExtInfoGroup": ciscoDs0BundleExtInfoGroup}
)
