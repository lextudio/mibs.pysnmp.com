# SNMP MIB module (ASCEND-MIBOSPFINR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBOSPFINR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:58 2024
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

_MibospfAreaRangeProfile_ObjectIdentity = ObjectIdentity
mibospfAreaRangeProfile = _MibospfAreaRangeProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 97)
)
_MibospfAreaRangeProfileTable_Object = MibTable
mibospfAreaRangeProfileTable = _MibospfAreaRangeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 97, 1)
)
if mibBuilder.loadTexts:
    mibospfAreaRangeProfileTable.setStatus("mandatory")
_MibospfAreaRangeProfileEntry_Object = MibTableRow
mibospfAreaRangeProfileEntry = _MibospfAreaRangeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1)
)
mibospfAreaRangeProfileEntry.setIndexNames(
    (0, "ASCEND-MIBOSPFINR-MIB", "ospfAreaRangeProfile-Name"),
)
if mibBuilder.loadTexts:
    mibospfAreaRangeProfileEntry.setStatus("mandatory")
_OspfAreaRangeProfile_Name_Type = DisplayString
_OspfAreaRangeProfile_Name_Object = MibScalar
ospfAreaRangeProfile_Name = _OspfAreaRangeProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 1),
    _OspfAreaRangeProfile_Name_Type()
)
ospfAreaRangeProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRangeProfile_Name.setStatus("mandatory")
_OspfAreaRangeProfile_AreaId_Type = IpAddress
_OspfAreaRangeProfile_AreaId_Object = MibScalar
ospfAreaRangeProfile_AreaId = _OspfAreaRangeProfile_AreaId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 2),
    _OspfAreaRangeProfile_AreaId_Type()
)
ospfAreaRangeProfile_AreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAreaRangeProfile_AreaId.setStatus("mandatory")
_OspfAreaRangeProfile_AreaNetworkAddr_Type = IpAddress
_OspfAreaRangeProfile_AreaNetworkAddr_Object = MibScalar
ospfAreaRangeProfile_AreaNetworkAddr = _OspfAreaRangeProfile_AreaNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 3),
    _OspfAreaRangeProfile_AreaNetworkAddr_Type()
)
ospfAreaRangeProfile_AreaNetworkAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAreaRangeProfile_AreaNetworkAddr.setStatus("mandatory")
_OspfAreaRangeProfile_AreaNetworkMask_Type = IpAddress
_OspfAreaRangeProfile_AreaNetworkMask_Object = MibScalar
ospfAreaRangeProfile_AreaNetworkMask = _OspfAreaRangeProfile_AreaNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 4),
    _OspfAreaRangeProfile_AreaNetworkMask_Type()
)
ospfAreaRangeProfile_AreaNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAreaRangeProfile_AreaNetworkMask.setStatus("mandatory")


class _OspfAreaRangeProfile_Advertize_Type(Integer32):
    """Custom type ospfAreaRangeProfile_Advertize based on Integer32"""
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


_OspfAreaRangeProfile_Advertize_Type.__name__ = "Integer32"
_OspfAreaRangeProfile_Advertize_Object = MibScalar
ospfAreaRangeProfile_Advertize = _OspfAreaRangeProfile_Advertize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 5),
    _OspfAreaRangeProfile_Advertize_Type()
)
ospfAreaRangeProfile_Advertize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAreaRangeProfile_Advertize.setStatus("mandatory")


class _OspfAreaRangeProfile_Action_o_Type(Integer32):
    """Custom type ospfAreaRangeProfile_Action_o based on Integer32"""
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


_OspfAreaRangeProfile_Action_o_Type.__name__ = "Integer32"
_OspfAreaRangeProfile_Action_o_Object = MibScalar
ospfAreaRangeProfile_Action_o = _OspfAreaRangeProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 6),
    _OspfAreaRangeProfile_Action_o_Type()
)
ospfAreaRangeProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAreaRangeProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBOSPFINR-MIB",
    **{"DisplayString": DisplayString,
       "mibospfAreaRangeProfile": mibospfAreaRangeProfile,
       "mibospfAreaRangeProfileTable": mibospfAreaRangeProfileTable,
       "mibospfAreaRangeProfileEntry": mibospfAreaRangeProfileEntry,
       "ospfAreaRangeProfile-Name": ospfAreaRangeProfile_Name,
       "ospfAreaRangeProfile-AreaId": ospfAreaRangeProfile_AreaId,
       "ospfAreaRangeProfile-AreaNetworkAddr": ospfAreaRangeProfile_AreaNetworkAddr,
       "ospfAreaRangeProfile-AreaNetworkMask": ospfAreaRangeProfile_AreaNetworkMask,
       "ospfAreaRangeProfile-Advertize": ospfAreaRangeProfile_Advertize,
       "ospfAreaRangeProfile-Action-o": ospfAreaRangeProfile_Action_o}
)
