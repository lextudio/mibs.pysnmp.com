# SNMP MIB module (CENTILLION-DOT3-EXTENSIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-DOT3-EXTENSIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:02 2024
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

(extensions,) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "extensions")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnDot3Extensions_ObjectIdentity = ObjectIdentity
cnDot3Extensions = _CnDot3Extensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 4)
)
_CnDot3ExtnTable_Object = MibTable
cnDot3ExtnTable = _CnDot3ExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 4, 1)
)
if mibBuilder.loadTexts:
    cnDot3ExtnTable.setStatus("mandatory")
_CnDot3ExtnEntry_Object = MibTableRow
cnDot3ExtnEntry = _CnDot3ExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 4, 1, 1)
)
cnDot3ExtnEntry.setIndexNames(
    (0, "CENTILLION-DOT3-EXTENSIONS-MIB", "cnDot3ExtnIfIndex"),
)
if mibBuilder.loadTexts:
    cnDot3ExtnEntry.setStatus("mandatory")
_CnDot3ExtnIfIndex_Type = Integer32
_CnDot3ExtnIfIndex_Object = MibTableColumn
cnDot3ExtnIfIndex = _CnDot3ExtnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 4, 1, 1, 1),
    _CnDot3ExtnIfIndex_Type()
)
cnDot3ExtnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDot3ExtnIfIndex.setStatus("mandatory")


class _CnDot3ExtnIfAdminSpeed_Type(Integer32):
    """Custom type cnDot3ExtnIfAdminSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("forced10", 1),
          ("forced100", 2),
          ("forced1000", 4))
    )


_CnDot3ExtnIfAdminSpeed_Type.__name__ = "Integer32"
_CnDot3ExtnIfAdminSpeed_Object = MibTableColumn
cnDot3ExtnIfAdminSpeed = _CnDot3ExtnIfAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 4, 1, 1, 2),
    _CnDot3ExtnIfAdminSpeed_Type()
)
cnDot3ExtnIfAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDot3ExtnIfAdminSpeed.setStatus("mandatory")
_CnDot3ExtnIfOperSpeed_Type = Gauge32
_CnDot3ExtnIfOperSpeed_Object = MibTableColumn
cnDot3ExtnIfOperSpeed = _CnDot3ExtnIfOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 4, 1, 1, 3),
    _CnDot3ExtnIfOperSpeed_Type()
)
cnDot3ExtnIfOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDot3ExtnIfOperSpeed.setStatus("mandatory")


class _CnDot3ExtnIfAdminConnectionType_Type(Integer32):
    """Custom type cnDot3ExtnIfAdminConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("fullDuplex", 2),
          ("halfDuplex", 1))
    )


_CnDot3ExtnIfAdminConnectionType_Type.__name__ = "Integer32"
_CnDot3ExtnIfAdminConnectionType_Object = MibTableColumn
cnDot3ExtnIfAdminConnectionType = _CnDot3ExtnIfAdminConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 4, 1, 1, 4),
    _CnDot3ExtnIfAdminConnectionType_Type()
)
cnDot3ExtnIfAdminConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDot3ExtnIfAdminConnectionType.setStatus("mandatory")


class _CnDot3ExtnIfOperConnectionType_Type(Integer32):
    """Custom type cnDot3ExtnIfOperConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 2),
          ("halfDuplex", 1))
    )


_CnDot3ExtnIfOperConnectionType_Type.__name__ = "Integer32"
_CnDot3ExtnIfOperConnectionType_Object = MibTableColumn
cnDot3ExtnIfOperConnectionType = _CnDot3ExtnIfOperConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 4, 1, 1, 5),
    _CnDot3ExtnIfOperConnectionType_Type()
)
cnDot3ExtnIfOperConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDot3ExtnIfOperConnectionType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-DOT3-EXTENSIONS-MIB",
    **{"cnDot3Extensions": cnDot3Extensions,
       "cnDot3ExtnTable": cnDot3ExtnTable,
       "cnDot3ExtnEntry": cnDot3ExtnEntry,
       "cnDot3ExtnIfIndex": cnDot3ExtnIfIndex,
       "cnDot3ExtnIfAdminSpeed": cnDot3ExtnIfAdminSpeed,
       "cnDot3ExtnIfOperSpeed": cnDot3ExtnIfOperSpeed,
       "cnDot3ExtnIfAdminConnectionType": cnDot3ExtnIfAdminConnectionType,
       "cnDot3ExtnIfOperConnectionType": cnDot3ExtnIfOperConnectionType}
)
