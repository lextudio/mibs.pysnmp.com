# SNMP MIB module (CT-DAREGISTRY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-DAREGISTRY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:03 2024
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

(cabletron,) = mibBuilder.importSymbols(
    "CTRON-OIDS",
    "cabletron")

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

_CtSSA_ObjectIdentity = ObjectIdentity
ctSSA = _CtSSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497)
)
_CtDARegistryTable_Object = MibTable
ctDARegistryTable = _CtDARegistryTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 1)
)
if mibBuilder.loadTexts:
    ctDARegistryTable.setStatus("mandatory")
_CtDARegistryEntry_Object = MibTableRow
ctDARegistryEntry = _CtDARegistryEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 1, 1)
)
ctDARegistryEntry.setIndexNames(
    (0, "CT-DAREGISTRY-MIB", "ctDARegistryIndex"),
    (0, "CT-DAREGISTRY-MIB", "ctDARegistryInstance"),
)
if mibBuilder.loadTexts:
    ctDARegistryEntry.setStatus("mandatory")


class _CtDARegistryIndex_Type(Integer32):
    """Custom type ctDARegistryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CtDARegistryIndex_Type.__name__ = "Integer32"
_CtDARegistryIndex_Object = MibTableColumn
ctDARegistryIndex = _CtDARegistryIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 1),
    _CtDARegistryIndex_Type()
)
ctDARegistryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDARegistryIndex.setStatus("mandatory")


class _CtDARegistryInstance_Type(Integer32):
    """Custom type ctDARegistryInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CtDARegistryInstance_Type.__name__ = "Integer32"
_CtDARegistryInstance_Object = MibTableColumn
ctDARegistryInstance = _CtDARegistryInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 2),
    _CtDARegistryInstance_Type()
)
ctDARegistryInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDARegistryInstance.setStatus("mandatory")


class _CtDARegistryAdminStatus_Type(Integer32):
    """Custom type ctDARegistryAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_CtDARegistryAdminStatus_Type.__name__ = "Integer32"
_CtDARegistryAdminStatus_Object = MibTableColumn
ctDARegistryAdminStatus = _CtDARegistryAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 3),
    _CtDARegistryAdminStatus_Type()
)
ctDARegistryAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDARegistryAdminStatus.setStatus("mandatory")


class _CtDARegistryOperStatus_Type(Integer32):
    """Custom type ctDARegistryOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_CtDARegistryOperStatus_Type.__name__ = "Integer32"
_CtDARegistryOperStatus_Object = MibTableColumn
ctDARegistryOperStatus = _CtDARegistryOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 4),
    _CtDARegistryOperStatus_Type()
)
ctDARegistryOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDARegistryOperStatus.setStatus("mandatory")
_CtDARegistryLastChange_Type = TimeTicks
_CtDARegistryLastChange_Object = MibTableColumn
ctDARegistryLastChange = _CtDARegistryLastChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 5),
    _CtDARegistryLastChange_Type()
)
ctDARegistryLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDARegistryLastChange.setStatus("mandatory")


class _CtDARegistryDescr_Type(DisplayString):
    """Custom type ctDARegistryDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CtDARegistryDescr_Type.__name__ = "DisplayString"
_CtDARegistryDescr_Object = MibTableColumn
ctDARegistryDescr = _CtDARegistryDescr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 6),
    _CtDARegistryDescr_Type()
)
ctDARegistryDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDARegistryDescr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-DAREGISTRY-MIB",
    **{"DisplayString": DisplayString,
       "ctSSA": ctSSA,
       "ctDARegistryTable": ctDARegistryTable,
       "ctDARegistryEntry": ctDARegistryEntry,
       "ctDARegistryIndex": ctDARegistryIndex,
       "ctDARegistryInstance": ctDARegistryInstance,
       "ctDARegistryAdminStatus": ctDARegistryAdminStatus,
       "ctDARegistryOperStatus": ctDARegistryOperStatus,
       "ctDARegistryLastChange": ctDARegistryLastChange,
       "ctDARegistryDescr": ctDARegistryDescr}
)
