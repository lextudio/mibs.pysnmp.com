# SNMP MIB module (DLINK-3100-DELETEIMG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-3100-DELETEIMG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:50 2024
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

(rnd,) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd")

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

rlDeleteImg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142)
)
rlDeleteImg.setRevisions(
        ("2007-11-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DELETEIMGName(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("image1", 1),
          ("image2", 2),
          ("none", 0))
    )



# MIB Managed Objects in the order of their OIDs

_RlDeleteImgTable_Object = MibTable
rlDeleteImgTable = _RlDeleteImgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1)
)
if mibBuilder.loadTexts:
    rlDeleteImgTable.setStatus("current")
_RlDeleteImgEntry_Object = MibTableRow
rlDeleteImgEntry = _RlDeleteImgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1, 1)
)
rlDeleteImgEntry.setIndexNames(
    (0, "DLINK-3100-DELETEIMG-MIB", "rlDeleteImgKey"),
)
if mibBuilder.loadTexts:
    rlDeleteImgEntry.setStatus("current")


class _RlDeleteImgKey_Type(Integer32):
    """Custom type rlDeleteImgKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RlDeleteImgKey_Type.__name__ = "Integer32"
_RlDeleteImgKey_Object = MibTableColumn
rlDeleteImgKey = _RlDeleteImgKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1, 1, 1),
    _RlDeleteImgKey_Type()
)
rlDeleteImgKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDeleteImgKey.setStatus("current")
_RlDeleteImgUnit_Type = Integer32
_RlDeleteImgUnit_Object = MibTableColumn
rlDeleteImgUnit = _RlDeleteImgUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1, 1, 2),
    _RlDeleteImgUnit_Type()
)
rlDeleteImgUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDeleteImgUnit.setStatus("current")
_RlDeleteImgName_Type = DELETEIMGName
_RlDeleteImgName_Object = MibTableColumn
rlDeleteImgName = _RlDeleteImgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1, 1, 3),
    _RlDeleteImgName_Type()
)
rlDeleteImgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDeleteImgName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-DELETEIMG-MIB",
    **{"DELETEIMGName": DELETEIMGName,
       "rlDeleteImg": rlDeleteImg,
       "rlDeleteImgTable": rlDeleteImgTable,
       "rlDeleteImgEntry": rlDeleteImgEntry,
       "rlDeleteImgKey": rlDeleteImgKey,
       "rlDeleteImgUnit": rlDeleteImgUnit,
       "rlDeleteImgName": rlDeleteImgName}
)
