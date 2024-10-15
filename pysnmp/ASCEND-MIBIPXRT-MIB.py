# SNMP MIB module (ASCEND-MIBIPXRT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBIPXRT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:48 2024
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

_MibipxRouteProfile_ObjectIdentity = ObjectIdentity
mibipxRouteProfile = _MibipxRouteProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 89)
)
_MibipxRouteProfileTable_Object = MibTable
mibipxRouteProfileTable = _MibipxRouteProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 89, 1)
)
if mibBuilder.loadTexts:
    mibipxRouteProfileTable.setStatus("mandatory")
_MibipxRouteProfileEntry_Object = MibTableRow
mibipxRouteProfileEntry = _MibipxRouteProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 89, 1, 1)
)
mibipxRouteProfileEntry.setIndexNames(
    (0, "ASCEND-MIBIPXRT-MIB", "ipxRouteProfile-Name"),
)
if mibBuilder.loadTexts:
    mibipxRouteProfileEntry.setStatus("mandatory")
_IpxRouteProfile_Index_Type = Integer32
_IpxRouteProfile_Index_Object = MibScalar
ipxRouteProfile_Index = _IpxRouteProfile_Index_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 89, 1, 1, 1),
    _IpxRouteProfile_Index_Type()
)
ipxRouteProfile_Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteProfile_Index.setStatus("mandatory")
_IpxRouteProfile_Name_Type = DisplayString
_IpxRouteProfile_Name_Object = MibScalar
ipxRouteProfile_Name = _IpxRouteProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 89, 1, 1, 2),
    _IpxRouteProfile_Name_Type()
)
ipxRouteProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRouteProfile_Name.setStatus("mandatory")
_IpxRouteProfile_ServerType_Type = DisplayString
_IpxRouteProfile_ServerType_Object = MibScalar
ipxRouteProfile_ServerType = _IpxRouteProfile_ServerType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 89, 1, 1, 3),
    _IpxRouteProfile_ServerType_Type()
)
ipxRouteProfile_ServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteProfile_ServerType.setStatus("mandatory")
_IpxRouteProfile_DestNetwork_Type = DisplayString
_IpxRouteProfile_DestNetwork_Object = MibScalar
ipxRouteProfile_DestNetwork = _IpxRouteProfile_DestNetwork_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 89, 1, 1, 4),
    _IpxRouteProfile_DestNetwork_Type()
)
ipxRouteProfile_DestNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteProfile_DestNetwork.setStatus("mandatory")
_IpxRouteProfile_ServerNode_Type = DisplayString
_IpxRouteProfile_ServerNode_Object = MibScalar
ipxRouteProfile_ServerNode = _IpxRouteProfile_ServerNode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 89, 1, 1, 5),
    _IpxRouteProfile_ServerNode_Type()
)
ipxRouteProfile_ServerNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteProfile_ServerNode.setStatus("mandatory")
_IpxRouteProfile_ServerSocket_Type = DisplayString
_IpxRouteProfile_ServerSocket_Object = MibScalar
ipxRouteProfile_ServerSocket = _IpxRouteProfile_ServerSocket_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 89, 1, 1, 6),
    _IpxRouteProfile_ServerSocket_Type()
)
ipxRouteProfile_ServerSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteProfile_ServerSocket.setStatus("mandatory")
_IpxRouteProfile_Hops_Type = Integer32
_IpxRouteProfile_Hops_Object = MibScalar
ipxRouteProfile_Hops = _IpxRouteProfile_Hops_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 89, 1, 1, 7),
    _IpxRouteProfile_Hops_Type()
)
ipxRouteProfile_Hops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteProfile_Hops.setStatus("mandatory")
_IpxRouteProfile_Ticks_Type = Integer32
_IpxRouteProfile_Ticks_Object = MibScalar
ipxRouteProfile_Ticks = _IpxRouteProfile_Ticks_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 89, 1, 1, 8),
    _IpxRouteProfile_Ticks_Type()
)
ipxRouteProfile_Ticks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteProfile_Ticks.setStatus("mandatory")
_IpxRouteProfile_ProfileNumber_Type = Integer32
_IpxRouteProfile_ProfileNumber_Object = MibScalar
ipxRouteProfile_ProfileNumber = _IpxRouteProfile_ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 89, 1, 1, 9),
    _IpxRouteProfile_ProfileNumber_Type()
)
ipxRouteProfile_ProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteProfile_ProfileNumber.setStatus("mandatory")
_IpxRouteProfile_ProfileName_Type = DisplayString
_IpxRouteProfile_ProfileName_Object = MibScalar
ipxRouteProfile_ProfileName = _IpxRouteProfile_ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 89, 1, 1, 10),
    _IpxRouteProfile_ProfileName_Type()
)
ipxRouteProfile_ProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteProfile_ProfileName.setStatus("mandatory")


class _IpxRouteProfile_ActiveRoute_Type(Integer32):
    """Custom type ipxRouteProfile_ActiveRoute based on Integer32"""
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


_IpxRouteProfile_ActiveRoute_Type.__name__ = "Integer32"
_IpxRouteProfile_ActiveRoute_Object = MibScalar
ipxRouteProfile_ActiveRoute = _IpxRouteProfile_ActiveRoute_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 89, 1, 1, 11),
    _IpxRouteProfile_ActiveRoute_Type()
)
ipxRouteProfile_ActiveRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteProfile_ActiveRoute.setStatus("mandatory")


class _IpxRouteProfile_Action_o_Type(Integer32):
    """Custom type ipxRouteProfile_Action_o based on Integer32"""
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


_IpxRouteProfile_Action_o_Type.__name__ = "Integer32"
_IpxRouteProfile_Action_o_Object = MibScalar
ipxRouteProfile_Action_o = _IpxRouteProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 89, 1, 1, 12),
    _IpxRouteProfile_Action_o_Type()
)
ipxRouteProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBIPXRT-MIB",
    **{"DisplayString": DisplayString,
       "mibipxRouteProfile": mibipxRouteProfile,
       "mibipxRouteProfileTable": mibipxRouteProfileTable,
       "mibipxRouteProfileEntry": mibipxRouteProfileEntry,
       "ipxRouteProfile-Index": ipxRouteProfile_Index,
       "ipxRouteProfile-Name": ipxRouteProfile_Name,
       "ipxRouteProfile-ServerType": ipxRouteProfile_ServerType,
       "ipxRouteProfile-DestNetwork": ipxRouteProfile_DestNetwork,
       "ipxRouteProfile-ServerNode": ipxRouteProfile_ServerNode,
       "ipxRouteProfile-ServerSocket": ipxRouteProfile_ServerSocket,
       "ipxRouteProfile-Hops": ipxRouteProfile_Hops,
       "ipxRouteProfile-Ticks": ipxRouteProfile_Ticks,
       "ipxRouteProfile-ProfileNumber": ipxRouteProfile_ProfileNumber,
       "ipxRouteProfile-ProfileName": ipxRouteProfile_ProfileName,
       "ipxRouteProfile-ActiveRoute": ipxRouteProfile_ActiveRoute,
       "ipxRouteProfile-Action-o": ipxRouteProfile_Action_o}
)
