# SNMP MIB module (ASCEND-MIBOSPFNBMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBOSPFNBMA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:59 2024
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

_MibospfNbmaNeighborProfile_ObjectIdentity = ObjectIdentity
mibospfNbmaNeighborProfile = _MibospfNbmaNeighborProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 98)
)
_MibospfNbmaNeighborProfileTable_Object = MibTable
mibospfNbmaNeighborProfileTable = _MibospfNbmaNeighborProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 98, 1)
)
if mibBuilder.loadTexts:
    mibospfNbmaNeighborProfileTable.setStatus("mandatory")
_MibospfNbmaNeighborProfileEntry_Object = MibTableRow
mibospfNbmaNeighborProfileEntry = _MibospfNbmaNeighborProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1)
)
mibospfNbmaNeighborProfileEntry.setIndexNames(
    (0, "ASCEND-MIBOSPFNBMA-MIB", "ospfNbmaNeighborProfile-Name"),
)
if mibBuilder.loadTexts:
    mibospfNbmaNeighborProfileEntry.setStatus("mandatory")
_OspfNbmaNeighborProfile_Name_Type = DisplayString
_OspfNbmaNeighborProfile_Name_Object = MibScalar
ospfNbmaNeighborProfile_Name = _OspfNbmaNeighborProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1, 1),
    _OspfNbmaNeighborProfile_Name_Type()
)
ospfNbmaNeighborProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbmaNeighborProfile_Name.setStatus("mandatory")
_OspfNbmaNeighborProfile_HostName_Type = DisplayString
_OspfNbmaNeighborProfile_HostName_Object = MibScalar
ospfNbmaNeighborProfile_HostName = _OspfNbmaNeighborProfile_HostName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1, 2),
    _OspfNbmaNeighborProfile_HostName_Type()
)
ospfNbmaNeighborProfile_HostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNbmaNeighborProfile_HostName.setStatus("mandatory")
_OspfNbmaNeighborProfile_IpAddress_Type = IpAddress
_OspfNbmaNeighborProfile_IpAddress_Object = MibScalar
ospfNbmaNeighborProfile_IpAddress = _OspfNbmaNeighborProfile_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1, 3),
    _OspfNbmaNeighborProfile_IpAddress_Type()
)
ospfNbmaNeighborProfile_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNbmaNeighborProfile_IpAddress.setStatus("mandatory")


class _OspfNbmaNeighborProfile_DrCapable_Type(Integer32):
    """Custom type ospfNbmaNeighborProfile_DrCapable based on Integer32"""
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


_OspfNbmaNeighborProfile_DrCapable_Type.__name__ = "Integer32"
_OspfNbmaNeighborProfile_DrCapable_Object = MibScalar
ospfNbmaNeighborProfile_DrCapable = _OspfNbmaNeighborProfile_DrCapable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1, 4),
    _OspfNbmaNeighborProfile_DrCapable_Type()
)
ospfNbmaNeighborProfile_DrCapable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNbmaNeighborProfile_DrCapable.setStatus("mandatory")


class _OspfNbmaNeighborProfile_Action_o_Type(Integer32):
    """Custom type ospfNbmaNeighborProfile_Action_o based on Integer32"""
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


_OspfNbmaNeighborProfile_Action_o_Type.__name__ = "Integer32"
_OspfNbmaNeighborProfile_Action_o_Object = MibScalar
ospfNbmaNeighborProfile_Action_o = _OspfNbmaNeighborProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1, 5),
    _OspfNbmaNeighborProfile_Action_o_Type()
)
ospfNbmaNeighborProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNbmaNeighborProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBOSPFNBMA-MIB",
    **{"DisplayString": DisplayString,
       "mibospfNbmaNeighborProfile": mibospfNbmaNeighborProfile,
       "mibospfNbmaNeighborProfileTable": mibospfNbmaNeighborProfileTable,
       "mibospfNbmaNeighborProfileEntry": mibospfNbmaNeighborProfileEntry,
       "ospfNbmaNeighborProfile-Name": ospfNbmaNeighborProfile_Name,
       "ospfNbmaNeighborProfile-HostName": ospfNbmaNeighborProfile_HostName,
       "ospfNbmaNeighborProfile-IpAddress": ospfNbmaNeighborProfile_IpAddress,
       "ospfNbmaNeighborProfile-DrCapable": ospfNbmaNeighborProfile_DrCapable,
       "ospfNbmaNeighborProfile-Action-o": ospfNbmaNeighborProfile_Action_o}
)
