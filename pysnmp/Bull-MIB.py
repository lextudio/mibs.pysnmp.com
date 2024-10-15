# SNMP MIB module (Bull-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Bull-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:29 2024
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

_Bull_ObjectIdentity = ObjectIdentity
bull = _Bull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 107)
)
_Bull_products_ObjectIdentity = ObjectIdentity
bull_products = _Bull_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 107, 1)
)
_Bull_DPX2_ObjectIdentity = ObjectIdentity
bull_DPX2 = _Bull_DPX2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 107, 1, 1)
)


class _Bull_DPX2_100_Type(DisplayString):
    """Custom type bull_DPX2_100 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Bull_DPX2_100_Type.__name__ = "DisplayString"
_Bull_DPX2_100_Object = MibScalar
bull_DPX2_100 = _Bull_DPX2_100_Object(
    (1, 3, 6, 1, 4, 1, 107, 1, 1, 1),
    _Bull_DPX2_100_Type()
)
bull_DPX2_100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bull_DPX2_100.setStatus("optional")


class _Bull_DPX2_200_Type(DisplayString):
    """Custom type bull_DPX2_200 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Bull_DPX2_200_Type.__name__ = "DisplayString"
_Bull_DPX2_200_Object = MibScalar
bull_DPX2_200 = _Bull_DPX2_200_Object(
    (1, 3, 6, 1, 4, 1, 107, 1, 1, 2),
    _Bull_DPX2_200_Type()
)
bull_DPX2_200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bull_DPX2_200.setStatus("optional")


class _Bull_DPX2_300_Type(DisplayString):
    """Custom type bull_DPX2_300 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Bull_DPX2_300_Type.__name__ = "DisplayString"
_Bull_DPX2_300_Object = MibScalar
bull_DPX2_300 = _Bull_DPX2_300_Object(
    (1, 3, 6, 1, 4, 1, 107, 1, 1, 3),
    _Bull_DPX2_300_Type()
)
bull_DPX2_300.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bull_DPX2_300.setStatus("optional")
_Bull_mibs_ObjectIdentity = ObjectIdentity
bull_mibs = _Bull_mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 107, 2)
)
_Bull_mibs_mib1_ObjectIdentity = ObjectIdentity
bull_mibs_mib1 = _Bull_mibs_mib1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 107, 2, 1)
)
_Bull_System_ObjectIdentity = ObjectIdentity
bull_System = _Bull_System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 1)
)
_Bull_Streams_ObjectIdentity = ObjectIdentity
bull_Streams = _Bull_Streams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2)
)
_BullStrTable_Object = MibTable
bullStrTable = _BullStrTable_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    bullStrTable.setStatus("mandatory")
_BullStrEntry_Object = MibTableRow
bullStrEntry = _BullStrEntry_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 1, 1)
)
bullStrEntry.setIndexNames(
    (0, "Bull-MIB", "bullStrType"),
)
if mibBuilder.loadTexts:
    bullStrEntry.setStatus("mandatory")


class _BullStrType_Type(Integer32):
    """Custom type bullStrType based on Integer32"""
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
        *(("blocks", 4),
          ("messages", 3),
          ("queues", 2),
          ("streams", 1))
    )


_BullStrType_Type.__name__ = "Integer32"
_BullStrType_Object = MibTableColumn
bullStrType = _BullStrType_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 1, 1, 1),
    _BullStrType_Type()
)
bullStrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bullStrType.setStatus("mandatory")
_BullStrAlloc_Type = Integer32
_BullStrAlloc_Object = MibTableColumn
bullStrAlloc = _BullStrAlloc_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 1, 1, 2),
    _BullStrAlloc_Type()
)
bullStrAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bullStrAlloc.setStatus("mandatory")
_BullStrInuse_Type = Gauge32
_BullStrInuse_Object = MibTableColumn
bullStrInuse = _BullStrInuse_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 1, 1, 3),
    _BullStrInuse_Type()
)
bullStrInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bullStrInuse.setStatus("mandatory")
_BullStrMaxs_Type = Counter32
_BullStrMaxs_Object = MibTableColumn
bullStrMaxs = _BullStrMaxs_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 1, 1, 4),
    _BullStrMaxs_Type()
)
bullStrMaxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bullStrMaxs.setStatus("mandatory")
_BullStrTotals_Type = Counter32
_BullStrTotals_Object = MibTableColumn
bullStrTotals = _BullStrTotals_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 1, 1, 5),
    _BullStrTotals_Type()
)
bullStrTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bullStrTotals.setStatus("mandatory")
_BullStrFails_Type = Counter32
_BullStrFails_Object = MibTableColumn
bullStrFails = _BullStrFails_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 1, 1, 6),
    _BullStrFails_Type()
)
bullStrFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bullStrFails.setStatus("mandatory")
_BullBlkTable_Object = MibTable
bullBlkTable = _BullBlkTable_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    bullBlkTable.setStatus("mandatory")
_BullBlkEntry_Object = MibTableRow
bullBlkEntry = _BullBlkEntry_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1)
)
bullBlkEntry.setIndexNames(
    (0, "Bull-MIB", "bullBlkclass"),
)
if mibBuilder.loadTexts:
    bullBlkEntry.setStatus("mandatory")


class _BullBlkClass_Type(Integer32):
    """Custom type bullBlkClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BullBlkClass_Type.__name__ = "Integer32"
_BullBlkClass_Object = MibTableColumn
bullBlkClass = _BullBlkClass_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1, 1),
    _BullBlkClass_Type()
)
bullBlkClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bullBlkClass.setStatus("mandatory")
_BullBlkAlloc_Type = Integer32
_BullBlkAlloc_Object = MibTableColumn
bullBlkAlloc = _BullBlkAlloc_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1, 2),
    _BullBlkAlloc_Type()
)
bullBlkAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bullBlkAlloc.setStatus("mandatory")
_BullBlkInuse_Type = Gauge32
_BullBlkInuse_Object = MibTableColumn
bullBlkInuse = _BullBlkInuse_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1, 3),
    _BullBlkInuse_Type()
)
bullBlkInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bullBlkInuse.setStatus("mandatory")
_BullBlkLowpris_Type = Counter32
_BullBlkLowpris_Object = MibTableColumn
bullBlkLowpris = _BullBlkLowpris_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1, 5),
    _BullBlkLowpris_Type()
)
bullBlkLowpris.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bullBlkLowpris.setStatus("mandatory")
_BullBlkMedpris_Type = Counter32
_BullBlkMedpris_Object = MibTableColumn
bullBlkMedpris = _BullBlkMedpris_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1, 6),
    _BullBlkMedpris_Type()
)
bullBlkMedpris.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bullBlkMedpris.setStatus("mandatory")
_BullBlkMaxs_Type = Counter32
_BullBlkMaxs_Object = MibTableColumn
bullBlkMaxs = _BullBlkMaxs_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1, 7),
    _BullBlkMaxs_Type()
)
bullBlkMaxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bullBlkMaxs.setStatus("mandatory")
_BullBlkTotals_Type = Counter32
_BullBlkTotals_Object = MibTableColumn
bullBlkTotals = _BullBlkTotals_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1, 8),
    _BullBlkTotals_Type()
)
bullBlkTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bullBlkTotals.setStatus("mandatory")
_BullBlkFails_Type = Counter32
_BullBlkFails_Object = MibTableColumn
bullBlkFails = _BullBlkFails_Object(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1, 9),
    _BullBlkFails_Type()
)
bullBlkFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bullBlkFails.setStatus("mandatory")
_Bull_Ether_ObjectIdentity = ObjectIdentity
bull_Ether = _Bull_Ether_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 3)
)
_Bull_Serial_ObjectIdentity = ObjectIdentity
bull_Serial = _Bull_Serial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 4)
)
_Bull_X25_ObjectIdentity = ObjectIdentity
bull_X25 = _Bull_X25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 5)
)
_Bull_NMFX_ObjectIdentity = ObjectIdentity
bull_NMFX = _Bull_NMFX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 107, 2, 1, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Bull-MIB",
    **{"bull": bull,
       "bull-products": bull_products,
       "bull-DPX2": bull_DPX2,
       "bull-DPX2-100": bull_DPX2_100,
       "bull-DPX2-200": bull_DPX2_200,
       "bull-DPX2-300": bull_DPX2_300,
       "bull-mibs": bull_mibs,
       "bull-mibs-mib1": bull_mibs_mib1,
       "bull-System": bull_System,
       "bull-Streams": bull_Streams,
       "bullStrTable": bullStrTable,
       "bullStrEntry": bullStrEntry,
       "bullStrType": bullStrType,
       "bullStrAlloc": bullStrAlloc,
       "bullStrInuse": bullStrInuse,
       "bullStrMaxs": bullStrMaxs,
       "bullStrTotals": bullStrTotals,
       "bullStrFails": bullStrFails,
       "bullBlkTable": bullBlkTable,
       "bullBlkEntry": bullBlkEntry,
       "bullBlkClass": bullBlkClass,
       "bullBlkAlloc": bullBlkAlloc,
       "bullBlkInuse": bullBlkInuse,
       "bullBlkLowpris": bullBlkLowpris,
       "bullBlkMedpris": bullBlkMedpris,
       "bullBlkMaxs": bullBlkMaxs,
       "bullBlkTotals": bullBlkTotals,
       "bullBlkFails": bullBlkFails,
       "bull-Ether": bull_Ether,
       "bull-Serial": bull_Serial,
       "bull-X25": bull_X25,
       "bull-NMFX": bull_NMFX}
)
