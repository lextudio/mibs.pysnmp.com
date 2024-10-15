# SNMP MIB module (ADTRAN-ATLAS550-QUAD-BRI-U-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-ATLAS550-QUAD-BRI-U-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:28 2024
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

(adATLASBRIIfIndex,) = mibBuilder.importSymbols(
    "ADTRAN-ATLAS-BRI-MIB",
    "adATLASBRIIfIndex")

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
 enterprises,
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
    "enterprises",
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

_Adtran_ObjectIdentity = ObjectIdentity
adtran = _Adtran_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664)
)
_AdMgmt_ObjectIdentity = ObjectIdentity
adMgmt = _AdMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2)
)
_AdATLAS550QuadBRIUmg_ObjectIdentity = ObjectIdentity
adATLAS550QuadBRIUmg = _AdATLAS550QuadBRIUmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 274)
)
_AdATLAS550QuadBRIUIfTable_Object = MibTable
adATLAS550QuadBRIUIfTable = _AdATLAS550QuadBRIUIfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 274, 1)
)
if mibBuilder.loadTexts:
    adATLAS550QuadBRIUIfTable.setStatus("mandatory")
_AdATLAS550QuadBRIUIfEntry_Object = MibTableRow
adATLAS550QuadBRIUIfEntry = _AdATLAS550QuadBRIUIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 274, 1, 1)
)
adATLAS550QuadBRIUIfEntry.setIndexNames(
    (0, "ADTRAN-ATLAS550-QUAD-BRI-U-MIB", "adATLAS550QuadBRIUIfIndex"),
)
if mibBuilder.loadTexts:
    adATLAS550QuadBRIUIfEntry.setStatus("mandatory")
_AdATLAS550QuadBRIUIfIndex_Type = Integer32
_AdATLAS550QuadBRIUIfIndex_Object = MibTableColumn
adATLAS550QuadBRIUIfIndex = _AdATLAS550QuadBRIUIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 274, 1, 1, 1),
    _AdATLAS550QuadBRIUIfIndex_Type()
)
adATLAS550QuadBRIUIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAS550QuadBRIUIfIndex.setStatus("mandatory")
_AdATLAS550QuadBRIUIfNEBE_Type = Counter32
_AdATLAS550QuadBRIUIfNEBE_Object = MibTableColumn
adATLAS550QuadBRIUIfNEBE = _AdATLAS550QuadBRIUIfNEBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 274, 1, 1, 2),
    _AdATLAS550QuadBRIUIfNEBE_Type()
)
adATLAS550QuadBRIUIfNEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAS550QuadBRIUIfNEBE.setStatus("mandatory")
_AdATLAS550QuadBRIUIfFEBE_Type = Counter32
_AdATLAS550QuadBRIUIfFEBE_Object = MibTableColumn
adATLAS550QuadBRIUIfFEBE = _AdATLAS550QuadBRIUIfFEBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 274, 1, 1, 3),
    _AdATLAS550QuadBRIUIfFEBE_Type()
)
adATLAS550QuadBRIUIfFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAS550QuadBRIUIfFEBE.setStatus("mandatory")


class _AdATLAS550QuadBRIUIfResetBECounts_Type(Integer32):
    """Custom type adATLAS550QuadBRIUIfResetBECounts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetCounts", 1)
    )


_AdATLAS550QuadBRIUIfResetBECounts_Type.__name__ = "Integer32"
_AdATLAS550QuadBRIUIfResetBECounts_Object = MibTableColumn
adATLAS550QuadBRIUIfResetBECounts = _AdATLAS550QuadBRIUIfResetBECounts_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 274, 1, 1, 4),
    _AdATLAS550QuadBRIUIfResetBECounts_Type()
)
adATLAS550QuadBRIUIfResetBECounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLAS550QuadBRIUIfResetBECounts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-ATLAS550-QUAD-BRI-U-MIB",
    **{"adtran": adtran,
       "adMgmt": adMgmt,
       "adATLAS550QuadBRIUmg": adATLAS550QuadBRIUmg,
       "adATLAS550QuadBRIUIfTable": adATLAS550QuadBRIUIfTable,
       "adATLAS550QuadBRIUIfEntry": adATLAS550QuadBRIUIfEntry,
       "adATLAS550QuadBRIUIfIndex": adATLAS550QuadBRIUIfIndex,
       "adATLAS550QuadBRIUIfNEBE": adATLAS550QuadBRIUIfNEBE,
       "adATLAS550QuadBRIUIfFEBE": adATLAS550QuadBRIUIfFEBE,
       "adATLAS550QuadBRIUIfResetBECounts": adATLAS550QuadBRIUIfResetBECounts}
)
