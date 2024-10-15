# SNMP MIB module (OPTIX-SONET-CRS-MIB-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPTIX-SONET-CRS-MIB-V2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:29 2024
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

(optixProvisionSonet,) = mibBuilder.importSymbols(
    "OPTIX-OID-MIB",
    "optixProvisionSonet")

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

optixsonetCRS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RowStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )



# MIB Managed Objects in the order of their OIDs

_OptixsonetCrsTable_Object = MibTable
optixsonetCrsTable = _OptixsonetCrsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3)
)
if mibBuilder.loadTexts:
    optixsonetCrsTable.setStatus("current")
_OptixsonetCrsEntry_Object = MibTableRow
optixsonetCrsEntry = _OptixsonetCrsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1)
)
optixsonetCrsEntry.setIndexNames(
    (0, "OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsMod2"),
    (0, "OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsFrom"),
    (0, "OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsTo"),
    (0, "OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsCct"),
)
if mibBuilder.loadTexts:
    optixsonetCrsEntry.setStatus("current")


class _OptixsonetCrsMod2_Type(Integer32):
    """Custom type optixsonetCrsMod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9,
              10,
              11,
              12,
              13,
              15,
              16,
              17,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("crsSTS1", 9),
          ("crsSTS12C", 13),
          ("crsSTS192C", 17),
          ("crsSTS24C", 15),
          ("crsSTS3C", 10),
          ("crsSTS48C", 16),
          ("crsSTS6C", 11),
          ("crsSTS9C", 12),
          ("crsVT1", 21),
          ("crsVT2", 22))
    )


_OptixsonetCrsMod2_Type.__name__ = "Integer32"
_OptixsonetCrsMod2_Object = MibTableColumn
optixsonetCrsMod2 = _OptixsonetCrsMod2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 1),
    _OptixsonetCrsMod2_Type()
)
optixsonetCrsMod2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixsonetCrsMod2.setStatus("current")


class _OptixsonetCrsFrom_Type(OctetString):
    """Custom type optixsonetCrsFrom based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OptixsonetCrsFrom_Type.__name__ = "OctetString"
_OptixsonetCrsFrom_Object = MibTableColumn
optixsonetCrsFrom = _OptixsonetCrsFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 2),
    _OptixsonetCrsFrom_Type()
)
optixsonetCrsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixsonetCrsFrom.setStatus("current")


class _OptixsonetCrsTo_Type(OctetString):
    """Custom type optixsonetCrsTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OptixsonetCrsTo_Type.__name__ = "OctetString"
_OptixsonetCrsTo_Object = MibTableColumn
optixsonetCrsTo = _OptixsonetCrsTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 3),
    _OptixsonetCrsTo_Type()
)
optixsonetCrsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixsonetCrsTo.setStatus("current")


class _OptixsonetCrsCct_Type(Integer32):
    """Custom type optixsonetCrsCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneWay", 2),
          ("twoWay", 1))
    )


_OptixsonetCrsCct_Type.__name__ = "Integer32"
_OptixsonetCrsCct_Object = MibTableColumn
optixsonetCrsCct = _OptixsonetCrsCct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 4),
    _OptixsonetCrsCct_Type()
)
optixsonetCrsCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixsonetCrsCct.setStatus("current")


class _OptixsonetCrsCktId_Type(OctetString):
    """Custom type optixsonetCrsCktId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OptixsonetCrsCktId_Type.__name__ = "OctetString"
_OptixsonetCrsCktId_Object = MibTableColumn
optixsonetCrsCktId = _OptixsonetCrsCktId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 5),
    _OptixsonetCrsCktId_Type()
)
optixsonetCrsCktId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixsonetCrsCktId.setStatus("current")


class _OptixsonetCrsPreferredPath_Type(OctetString):
    """Custom type optixsonetCrsPreferredPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OptixsonetCrsPreferredPath_Type.__name__ = "OctetString"
_OptixsonetCrsPreferredPath_Object = MibTableColumn
optixsonetCrsPreferredPath = _OptixsonetCrsPreferredPath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 6),
    _OptixsonetCrsPreferredPath_Type()
)
optixsonetCrsPreferredPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixsonetCrsPreferredPath.setStatus("current")


class _OptixsonetCrsRDLD_Type(Integer32):
    """Custom type optixsonetCrsRDLD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rdld", 1),
          ("rdldDEA", 2))
    )


_OptixsonetCrsRDLD_Type.__name__ = "Integer32"
_OptixsonetCrsRDLD_Object = MibTableColumn
optixsonetCrsRDLD = _OptixsonetCrsRDLD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 7),
    _OptixsonetCrsRDLD_Type()
)
optixsonetCrsRDLD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixsonetCrsRDLD.setStatus("current")
_OptixsonetCrsActivePath_Type = OctetString
_OptixsonetCrsActivePath_Object = MibTableColumn
optixsonetCrsActivePath = _OptixsonetCrsActivePath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 8),
    _OptixsonetCrsActivePath_Type()
)
optixsonetCrsActivePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixsonetCrsActivePath.setStatus("current")
_OptixsonetCrsRowStatus_Type = RowStatus
_OptixsonetCrsRowStatus_Object = MibTableColumn
optixsonetCrsRowStatus = _OptixsonetCrsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 10),
    _OptixsonetCrsRowStatus_Type()
)
optixsonetCrsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixsonetCrsRowStatus.setStatus("current")
_OptixsonetCRSConformance_ObjectIdentity = ObjectIdentity
optixsonetCRSConformance = _OptixsonetCRSConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 4)
)
_OptixsonetCRSGroups_ObjectIdentity = ObjectIdentity
optixsonetCRSGroups = _OptixsonetCRSGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 4, 1)
)
_OptixsonetCRSCompliances_ObjectIdentity = ObjectIdentity
optixsonetCRSCompliances = _OptixsonetCRSCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 4, 2)
)

# Managed Objects groups

currentObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 4, 1, 1)
)
currentObjectGroup.setObjects(
      *(("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsMod2"),
        ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsFrom"),
        ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsTo"),
        ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsCct"),
        ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsCktId"),
        ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsPreferredPath"),
        ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsRDLD"),
        ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsActivePath"),
        ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsRowStatus"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

basicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-SONET-CRS-MIB-V2",
    **{"RowStatus": RowStatus,
       "optixsonetCRS": optixsonetCRS,
       "optixsonetCrsTable": optixsonetCrsTable,
       "optixsonetCrsEntry": optixsonetCrsEntry,
       "optixsonetCrsMod2": optixsonetCrsMod2,
       "optixsonetCrsFrom": optixsonetCrsFrom,
       "optixsonetCrsTo": optixsonetCrsTo,
       "optixsonetCrsCct": optixsonetCrsCct,
       "optixsonetCrsCktId": optixsonetCrsCktId,
       "optixsonetCrsPreferredPath": optixsonetCrsPreferredPath,
       "optixsonetCrsRDLD": optixsonetCrsRDLD,
       "optixsonetCrsActivePath": optixsonetCrsActivePath,
       "optixsonetCrsRowStatus": optixsonetCrsRowStatus,
       "optixsonetCRSConformance": optixsonetCRSConformance,
       "optixsonetCRSGroups": optixsonetCRSGroups,
       "currentObjectGroup": currentObjectGroup,
       "optixsonetCRSCompliances": optixsonetCRSCompliances,
       "basicCompliance": basicCompliance}
)
