# SNMP MIB module (ASCEND-MIBPRROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBPRROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:04 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibprivateRouteTableProfile_ObjectIdentity = ObjectIdentity
mibprivateRouteTableProfile = _MibprivateRouteTableProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 103)
)
_MibprivateRouteTableProfileTable_Object = MibTable
mibprivateRouteTableProfileTable = _MibprivateRouteTableProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 103, 1)
)
if mibBuilder.loadTexts:
    mibprivateRouteTableProfileTable.setStatus("mandatory")
_MibprivateRouteTableProfileEntry_Object = MibTableRow
mibprivateRouteTableProfileEntry = _MibprivateRouteTableProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 103, 1, 1)
)
mibprivateRouteTableProfileEntry.setIndexNames(
    (0, "ASCEND-MIBPRROUTE-MIB", "privateRouteTableProfile-Name"),
)
if mibBuilder.loadTexts:
    mibprivateRouteTableProfileEntry.setStatus("mandatory")
_PrivateRouteTableProfile_Name_Type = DisplayString
_PrivateRouteTableProfile_Name_Object = MibScalar
privateRouteTableProfile_Name = _PrivateRouteTableProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 103, 1, 1, 1),
    _PrivateRouteTableProfile_Name_Type()
)
privateRouteTableProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privateRouteTableProfile_Name.setStatus("mandatory")


class _PrivateRouteTableProfile_Action_o_Type(Integer32):
    """Custom type privateRouteTableProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_PrivateRouteTableProfile_Action_o_Type.__name__ = "Integer32"
_PrivateRouteTableProfile_Action_o_Object = MibScalar
privateRouteTableProfile_Action_o = _PrivateRouteTableProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 103, 1, 1, 2),
    _PrivateRouteTableProfile_Action_o_Type()
)
privateRouteTableProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateRouteTableProfile_Action_o.setStatus("mandatory")
_MibprivateRouteTableProfile_RouteDescriptionListTable_Object = MibTable
mibprivateRouteTableProfile_RouteDescriptionListTable = _MibprivateRouteTableProfile_RouteDescriptionListTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 103, 2)
)
if mibBuilder.loadTexts:
    mibprivateRouteTableProfile_RouteDescriptionListTable.setStatus("mandatory")
_MibprivateRouteTableProfile_RouteDescriptionListEntry_Object = MibTableRow
mibprivateRouteTableProfile_RouteDescriptionListEntry = _MibprivateRouteTableProfile_RouteDescriptionListEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 103, 2, 1)
)
mibprivateRouteTableProfile_RouteDescriptionListEntry.setIndexNames(
    (0, "ASCEND-MIBPRROUTE-MIB", "privateRouteTableProfile-RouteDescriptionList-Name"),
    (0, "ASCEND-MIBPRROUTE-MIB", "privateRouteTableProfile-RouteDescriptionList-Index-o"),
)
if mibBuilder.loadTexts:
    mibprivateRouteTableProfile_RouteDescriptionListEntry.setStatus("mandatory")
_PrivateRouteTableProfile_RouteDescriptionList_Name_Type = DisplayString
_PrivateRouteTableProfile_RouteDescriptionList_Name_Object = MibScalar
privateRouteTableProfile_RouteDescriptionList_Name = _PrivateRouteTableProfile_RouteDescriptionList_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 103, 2, 1, 1),
    _PrivateRouteTableProfile_RouteDescriptionList_Name_Type()
)
privateRouteTableProfile_RouteDescriptionList_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privateRouteTableProfile_RouteDescriptionList_Name.setStatus("mandatory")
_PrivateRouteTableProfile_RouteDescriptionList_Index_o_Type = Integer32
_PrivateRouteTableProfile_RouteDescriptionList_Index_o_Object = MibScalar
privateRouteTableProfile_RouteDescriptionList_Index_o = _PrivateRouteTableProfile_RouteDescriptionList_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 103, 2, 1, 2),
    _PrivateRouteTableProfile_RouteDescriptionList_Index_o_Type()
)
privateRouteTableProfile_RouteDescriptionList_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privateRouteTableProfile_RouteDescriptionList_Index_o.setStatus("mandatory")


class _PrivateRouteTableProfile_RouteDescriptionList_Enabled_Type(Integer32):
    """Custom type privateRouteTableProfile_RouteDescriptionList_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrivateRouteTableProfile_RouteDescriptionList_Enabled_Type.__name__ = "Integer32"
_PrivateRouteTableProfile_RouteDescriptionList_Enabled_Object = MibScalar
privateRouteTableProfile_RouteDescriptionList_Enabled = _PrivateRouteTableProfile_RouteDescriptionList_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 103, 2, 1, 3),
    _PrivateRouteTableProfile_RouteDescriptionList_Enabled_Type()
)
privateRouteTableProfile_RouteDescriptionList_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateRouteTableProfile_RouteDescriptionList_Enabled.setStatus("mandatory")
_PrivateRouteTableProfile_RouteDescriptionList_DestAddress_Type = IpAddress
_PrivateRouteTableProfile_RouteDescriptionList_DestAddress_Object = MibScalar
privateRouteTableProfile_RouteDescriptionList_DestAddress = _PrivateRouteTableProfile_RouteDescriptionList_DestAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 103, 2, 1, 4),
    _PrivateRouteTableProfile_RouteDescriptionList_DestAddress_Type()
)
privateRouteTableProfile_RouteDescriptionList_DestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateRouteTableProfile_RouteDescriptionList_DestAddress.setStatus("mandatory")
_PrivateRouteTableProfile_RouteDescriptionList_Netmask_Type = IpAddress
_PrivateRouteTableProfile_RouteDescriptionList_Netmask_Object = MibScalar
privateRouteTableProfile_RouteDescriptionList_Netmask = _PrivateRouteTableProfile_RouteDescriptionList_Netmask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 103, 2, 1, 5),
    _PrivateRouteTableProfile_RouteDescriptionList_Netmask_Type()
)
privateRouteTableProfile_RouteDescriptionList_Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateRouteTableProfile_RouteDescriptionList_Netmask.setStatus("mandatory")
_PrivateRouteTableProfile_RouteDescriptionList_GatewayAddress_Type = IpAddress
_PrivateRouteTableProfile_RouteDescriptionList_GatewayAddress_Object = MibScalar
privateRouteTableProfile_RouteDescriptionList_GatewayAddress = _PrivateRouteTableProfile_RouteDescriptionList_GatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 103, 2, 1, 6),
    _PrivateRouteTableProfile_RouteDescriptionList_GatewayAddress_Type()
)
privateRouteTableProfile_RouteDescriptionList_GatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateRouteTableProfile_RouteDescriptionList_GatewayAddress.setStatus("mandatory")
_PrivateRouteTableProfile_RouteDescriptionList_Metric_Type = Integer32
_PrivateRouteTableProfile_RouteDescriptionList_Metric_Object = MibScalar
privateRouteTableProfile_RouteDescriptionList_Metric = _PrivateRouteTableProfile_RouteDescriptionList_Metric_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 103, 2, 1, 7),
    _PrivateRouteTableProfile_RouteDescriptionList_Metric_Type()
)
privateRouteTableProfile_RouteDescriptionList_Metric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateRouteTableProfile_RouteDescriptionList_Metric.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBPRROUTE-MIB",
    **{"DisplayString": DisplayString,
       "mibprivateRouteTableProfile": mibprivateRouteTableProfile,
       "mibprivateRouteTableProfileTable": mibprivateRouteTableProfileTable,
       "mibprivateRouteTableProfileEntry": mibprivateRouteTableProfileEntry,
       "privateRouteTableProfile-Name": privateRouteTableProfile_Name,
       "privateRouteTableProfile-Action-o": privateRouteTableProfile_Action_o,
       "mibprivateRouteTableProfile-RouteDescriptionListTable": mibprivateRouteTableProfile_RouteDescriptionListTable,
       "mibprivateRouteTableProfile-RouteDescriptionListEntry": mibprivateRouteTableProfile_RouteDescriptionListEntry,
       "privateRouteTableProfile-RouteDescriptionList-Name": privateRouteTableProfile_RouteDescriptionList_Name,
       "privateRouteTableProfile-RouteDescriptionList-Index-o": privateRouteTableProfile_RouteDescriptionList_Index_o,
       "privateRouteTableProfile-RouteDescriptionList-Enabled": privateRouteTableProfile_RouteDescriptionList_Enabled,
       "privateRouteTableProfile-RouteDescriptionList-DestAddress": privateRouteTableProfile_RouteDescriptionList_DestAddress,
       "privateRouteTableProfile-RouteDescriptionList-Netmask": privateRouteTableProfile_RouteDescriptionList_Netmask,
       "privateRouteTableProfile-RouteDescriptionList-GatewayAddress": privateRouteTableProfile_RouteDescriptionList_GatewayAddress,
       "privateRouteTableProfile-RouteDescriptionList-Metric": privateRouteTableProfile_RouteDescriptionList_Metric}
)
