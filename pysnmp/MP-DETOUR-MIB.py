# SNMP MIB module (MP-DETOUR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MP-DETOUR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:45 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "mgmt")

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

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Nec_ObjectIdentity = ObjectIdentity
nec = _Nec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119)
)
_NecProduct_ObjectIdentity = ObjectIdentity
necProduct = _NecProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 1)
)
_Datax_ObjectIdentity = ObjectIdentity
datax = _Datax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 1, 3)
)
_Mmpf_ObjectIdentity = ObjectIdentity
mmpf = _Mmpf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 1, 3, 13)
)
_Mmn9110_ObjectIdentity = ObjectIdentity
mmn9110 = _Mmn9110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 1, 3, 13, 1)
)
_Mmn9120_ObjectIdentity = ObjectIdentity
mmn9120 = _Mmn9120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 1, 3, 13, 2)
)
_Nec_mib_ObjectIdentity = ObjectIdentity
nec_mib = _Nec_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2)
)
_NecProductDepend_ObjectIdentity = ObjectIdentity
necProductDepend = _NecProductDepend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3)
)
_Datax_mib_ObjectIdentity = ObjectIdentity
datax_mib = _Datax_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3)
)
_Mmpf_mib_ObjectIdentity = ObjectIdentity
mmpf_mib = _Mmpf_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13)
)
_MpDetour_ObjectIdentity = ObjectIdentity
mpDetour = _MpDetour_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130)
)
_MpDetourTable_Object = MibTable
mpDetourTable = _MpDetourTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1)
)
if mibBuilder.loadTexts:
    mpDetourTable.setStatus("mandatory")
_MpDetourEntry_Object = MibTableRow
mpDetourEntry = _MpDetourEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1)
)
mpDetourEntry.setIndexNames(
    (0, "MP-DETOUR-MIB", "mpDetourID"),
)
if mibBuilder.loadTexts:
    mpDetourEntry.setStatus("mandatory")
_MpDetourID_Type = Integer32
_MpDetourID_Object = MibTableColumn
mpDetourID = _MpDetourID_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 1),
    _MpDetourID_Type()
)
mpDetourID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpDetourID.setStatus("mandatory")
_MpObservationIfindex_Type = Integer32
_MpObservationIfindex_Object = MibTableColumn
mpObservationIfindex = _MpObservationIfindex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 2),
    _MpObservationIfindex_Type()
)
mpObservationIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpObservationIfindex.setStatus("mandatory")


class _MpObservationIfType_Type(Integer32):
    """Custom type mpObservationIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("atmpp", 1),
          ("frpp", 7),
          ("lis", 3),
          ("mplspp", 9),
          ("outband", 4),
          ("ppp", 6),
          ("trunk", 5),
          ("vlan", 2),
          ("vlantrap", 8))
    )


_MpObservationIfType_Type.__name__ = "Integer32"
_MpObservationIfType_Object = MibTableColumn
mpObservationIfType = _MpObservationIfType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 3),
    _MpObservationIfType_Type()
)
mpObservationIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpObservationIfType.setStatus("mandatory")
_MpObservationIfNumber_Type = Integer32
_MpObservationIfNumber_Object = MibTableColumn
mpObservationIfNumber = _MpObservationIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 4),
    _MpObservationIfNumber_Type()
)
mpObservationIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpObservationIfNumber.setStatus("mandatory")
_MpDetourIfindex_Type = Integer32
_MpDetourIfindex_Object = MibTableColumn
mpDetourIfindex = _MpDetourIfindex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 5),
    _MpDetourIfindex_Type()
)
mpDetourIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpDetourIfindex.setStatus("mandatory")


class _MpDetourIfType_Type(Integer32):
    """Custom type mpDetourIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("atmpp", 1),
          ("frpp", 7),
          ("lis", 3),
          ("mplspp", 9),
          ("outband", 4),
          ("ppp", 6),
          ("trunk", 5),
          ("vlan", 2),
          ("vlantrap", 8))
    )


_MpDetourIfType_Type.__name__ = "Integer32"
_MpDetourIfType_Object = MibTableColumn
mpDetourIfType = _MpDetourIfType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 6),
    _MpDetourIfType_Type()
)
mpDetourIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpDetourIfType.setStatus("mandatory")
_MpDetourIfNumber_Type = Integer32
_MpDetourIfNumber_Object = MibTableColumn
mpDetourIfNumber = _MpDetourIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 7),
    _MpDetourIfNumber_Type()
)
mpDetourIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpDetourIfNumber.setStatus("mandatory")


class _MpObservationAdminStatus_Type(Integer32):
    """Custom type mpObservationAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpObservationAdminStatus_Type.__name__ = "Integer32"
_MpObservationAdminStatus_Object = MibTableColumn
mpObservationAdminStatus = _MpObservationAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 8),
    _MpObservationAdminStatus_Type()
)
mpObservationAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpObservationAdminStatus.setStatus("mandatory")


class _MpObservationOperStatus_Type(Integer32):
    """Custom type mpObservationOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpObservationOperStatus_Type.__name__ = "Integer32"
_MpObservationOperStatus_Object = MibTableColumn
mpObservationOperStatus = _MpObservationOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 9),
    _MpObservationOperStatus_Type()
)
mpObservationOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpObservationOperStatus.setStatus("mandatory")
_MpDiscardIfindex_Type = Integer32
_MpDiscardIfindex_Object = MibTableColumn
mpDiscardIfindex = _MpDiscardIfindex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 10),
    _MpDiscardIfindex_Type()
)
mpDiscardIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpDiscardIfindex.setStatus("mandatory")


class _MpDiscardIfType_Type(Integer32):
    """Custom type mpDiscardIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("atmpp", 1),
          ("frpp", 7),
          ("lis", 3),
          ("mplspp", 9),
          ("outband", 4),
          ("ppp", 6),
          ("trunk", 5),
          ("vlan", 2),
          ("vlantrap", 8))
    )


_MpDiscardIfType_Type.__name__ = "Integer32"
_MpDiscardIfType_Object = MibTableColumn
mpDiscardIfType = _MpDiscardIfType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 11),
    _MpDiscardIfType_Type()
)
mpDiscardIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpDiscardIfType.setStatus("mandatory")
_MpDiscardIfNumber_Type = Integer32
_MpDiscardIfNumber_Object = MibTableColumn
mpDiscardIfNumber = _MpDiscardIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 12),
    _MpDiscardIfNumber_Type()
)
mpDiscardIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpDiscardIfNumber.setStatus("mandatory")


class _MpDetourAdminStatus_Type(Integer32):
    """Custom type mpDetourAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpDetourAdminStatus_Type.__name__ = "Integer32"
_MpDetourAdminStatus_Object = MibTableColumn
mpDetourAdminStatus = _MpDetourAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 13),
    _MpDetourAdminStatus_Type()
)
mpDetourAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpDetourAdminStatus.setStatus("mandatory")


class _MpDetourOperStatus_Type(Integer32):
    """Custom type mpDetourOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpDetourOperStatus_Type.__name__ = "Integer32"
_MpDetourOperStatus_Object = MibTableColumn
mpDetourOperStatus = _MpDetourOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 14),
    _MpDetourOperStatus_Type()
)
mpDetourOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpDetourOperStatus.setStatus("mandatory")


class _MpDiscardAdminStatus_Type(Integer32):
    """Custom type mpDiscardAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpDiscardAdminStatus_Type.__name__ = "Integer32"
_MpDiscardAdminStatus_Object = MibTableColumn
mpDiscardAdminStatus = _MpDiscardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 15),
    _MpDiscardAdminStatus_Type()
)
mpDiscardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpDiscardAdminStatus.setStatus("mandatory")


class _MpDiscardOperStatus_Type(Integer32):
    """Custom type mpDiscardOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpDiscardOperStatus_Type.__name__ = "Integer32"
_MpDiscardOperStatus_Object = MibTableColumn
mpDiscardOperStatus = _MpDiscardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 16),
    _MpDiscardOperStatus_Type()
)
mpDiscardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpDiscardOperStatus.setStatus("mandatory")


class _MpRouteStatus_Type(Integer32):
    """Custom type mpRouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MpRouteStatus_Type.__name__ = "Integer32"
_MpRouteStatus_Object = MibTableColumn
mpRouteStatus = _MpRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 17),
    _MpRouteStatus_Type()
)
mpRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpRouteStatus.setStatus("mandatory")


class _MpInhibitMode_Type(Integer32):
    """Custom type mpInhibitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_MpInhibitMode_Type.__name__ = "Integer32"
_MpInhibitMode_Object = MibTableColumn
mpInhibitMode = _MpInhibitMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 18),
    _MpInhibitMode_Type()
)
mpInhibitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpInhibitMode.setStatus("mandatory")


class _MpWatchMode_Type(Integer32):
    """Custom type mpWatchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_MpWatchMode_Type.__name__ = "Integer32"
_MpWatchMode_Object = MibTableColumn
mpWatchMode = _MpWatchMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 1, 1, 19),
    _MpWatchMode_Type()
)
mpWatchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWatchMode.setStatus("mandatory")
_MpDetourConfigChangeTimeStamp_ObjectIdentity = ObjectIdentity
mpDetourConfigChangeTimeStamp = _MpDetourConfigChangeTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 2)
)
_MpDetourConfigLastChange_Type = TimeTicks
_MpDetourConfigLastChange_Object = MibScalar
mpDetourConfigLastChange = _MpDetourConfigLastChange_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 2, 1),
    _MpDetourConfigLastChange_Type()
)
mpDetourConfigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpDetourConfigLastChange.setStatus("mandatory")
_MpDetourStatusTimeStamp_ObjectIdentity = ObjectIdentity
mpDetourStatusTimeStamp = _MpDetourStatusTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 3)
)
_MpDetourStatusLastChange_Type = TimeTicks
_MpDetourStatusLastChange_Object = MibScalar
mpDetourStatusLastChange = _MpDetourStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 3, 13, 130, 3, 1),
    _MpDetourStatusLastChange_Type()
)
mpDetourStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpDetourStatusLastChange.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MP-DETOUR-MIB",
    **{"DisplayString": DisplayString,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "nec": nec,
       "necProduct": necProduct,
       "datax": datax,
       "mmpf": mmpf,
       "mmn9110": mmn9110,
       "mmn9120": mmn9120,
       "nec-mib": nec_mib,
       "necProductDepend": necProductDepend,
       "datax-mib": datax_mib,
       "mmpf-mib": mmpf_mib,
       "mpDetour": mpDetour,
       "mpDetourTable": mpDetourTable,
       "mpDetourEntry": mpDetourEntry,
       "mpDetourID": mpDetourID,
       "mpObservationIfindex": mpObservationIfindex,
       "mpObservationIfType": mpObservationIfType,
       "mpObservationIfNumber": mpObservationIfNumber,
       "mpDetourIfindex": mpDetourIfindex,
       "mpDetourIfType": mpDetourIfType,
       "mpDetourIfNumber": mpDetourIfNumber,
       "mpObservationAdminStatus": mpObservationAdminStatus,
       "mpObservationOperStatus": mpObservationOperStatus,
       "mpDiscardIfindex": mpDiscardIfindex,
       "mpDiscardIfType": mpDiscardIfType,
       "mpDiscardIfNumber": mpDiscardIfNumber,
       "mpDetourAdminStatus": mpDetourAdminStatus,
       "mpDetourOperStatus": mpDetourOperStatus,
       "mpDiscardAdminStatus": mpDiscardAdminStatus,
       "mpDiscardOperStatus": mpDiscardOperStatus,
       "mpRouteStatus": mpRouteStatus,
       "mpInhibitMode": mpInhibitMode,
       "mpWatchMode": mpWatchMode,
       "mpDetourConfigChangeTimeStamp": mpDetourConfigChangeTimeStamp,
       "mpDetourConfigLastChange": mpDetourConfigLastChange,
       "mpDetourStatusTimeStamp": mpDetourStatusTimeStamp,
       "mpDetourStatusLastChange": mpDetourStatusLastChange}
)
